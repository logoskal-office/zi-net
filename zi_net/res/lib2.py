import logging
import requests
from django.http import JsonResponse
from django.utils.timezone import now

# Configure logging
logging.basicConfig(
    filename="ip_lookup.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_client_ip(request):
    """Extracts the client's IP address from the Django request object."""
    try:
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        logging.info(f"Extracted IP: {ip}")
        return ip
    except Exception as e:
        logging.error(f"Error extracting IP: {str(e)}")
        return None

def fetch_ip_details(ip):
    """Fetches detailed information about an IP address using an external API."""
    try:
        api_url = f"https://ipapi.co/{ip}/json/"
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            logging.info(f"IP Details for {ip}: {data}")
            return data
        else:
            logging.warning(f"Failed to fetch IP details for {ip}: {response.status_code}")
            return None
    except requests.RequestException as e:
        logging.error(f"Request exception for IP {ip}: {str(e)}")
        return None

def get_request_meta(request):
    """Fetches meta information from the Django request object."""
    try:
        meta_info = {
            "method": request.method,
            "path": request.path,
            "content_type": request.content_type,
            "user_agent": request.META.get("HTTP_USER_AGENT", "Unknown"),
            "referrer": request.META.get("HTTP_REFERER", "Unknown"),
            "timestamp": now().isoformat(),
        }
        logging.info(f"Request Meta: {meta_info}")
        return meta_info
    except Exception as e:
        logging.error(f"Error fetching request meta: {str(e)}")
        return {}

def get_geo_distance(ip1, ip2):
    """Calculate approximate distance between two IP locations using latitude and longitude."""
    try:
        details1 = fetch_ip_details(ip1)
        details2 = fetch_ip_details(ip2)
        if not details1 or not details2:
            return None

        from math import radians, sin, cos, sqrt, atan2

        def haversine(lat1, lon1, lat2, lon2):
            R = 6371  # Earth radius in km
            dlat = radians(lat2 - lat1)
            dlon = radians(lon2 - lon1)
            a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            return R * c

        lat1, lon1 = float(details1.get("latitude", 0)), float(details1.get("longitude", 0))
        lat2, lon2 = float(details2.get("latitude", 0)), float(details2.get("longitude", 0))

        distance = haversine(lat1, lon1, lat2, lon2)
        logging.info(f"Distance between {ip1} and {ip2}: {distance} km")
        return distance
    except Exception as e:
        logging.error(f"Error calculating distance: {str(e)}")
        return None

def analyze_request(request):
    """Analyzes a Django request and returns comprehensive details."""
    try:
        ip = get_client_ip(request)
        if not ip:
            return JsonResponse({"error": "Unable to determine IP address."}, status=400)

        ip_details = fetch_ip_details(ip)
        request_meta = get_request_meta(request)

        if not ip_details:
            return JsonResponse({
                "error": "Failed to fetch IP details.",
                "request_meta": request_meta
            }, status=500)

        analysis = {
            "ip": ip,
            "ip_details": ip_details,
            "request_meta": request_meta
        }

        logging.info(f"Request Analysis: {analysis}")
        return JsonResponse(analysis, status=200)
    except Exception as e:
        logging.error(f"Error analyzing request: {str(e)}")
        return JsonResponse({"error": "Internal server error."}, status=500)

# Sample usage in a Django view
def request_analysis_view(request):
    """Django view that analyzes the incoming request."""
    return analyze_request(request)

# Additional utility: Fetch ISP and organization details
def fetch_isp_details(ip):
    """Fetch ISP and organization details for the IP address."""
    try:
        api_url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            isp_details = {
                "isp": data.get("org", "Unknown"),
                "asn": data.get("asn", "Unknown"),
                "ip_range": data.get("range", "Unknown")
            }
            logging.info(f"ISP Details for {ip}: {isp_details}")
            return isp_details
        else:
            logging.warning(f"Failed to fetch ISP details for {ip}: {response.status_code}")
            return None
    except requests.RequestException as e:
        logging.error(f"ISP request exception for IP {ip}: {str(e)}")
        return None

# Extended analysis to include ISP details
def analyze_request_extended(request):
    """Analyzes a Django request and returns comprehensive details, including ISP."""
    try:
        ip = get_client_ip(request)
        if not ip:
            return JsonResponse({"error": "Unable to determine IP address."}, status=400)

        ip_details = fetch_ip_details(ip)
        isp_details = fetch_isp_details(ip)
        request_meta = get_request_meta(request)

        if not ip_details:
            return JsonResponse({
                "error": "Failed to fetch IP details.",
                "request_meta": request_meta
            }, status=500)

        analysis = {
            "ip": ip,
            "ip_details": ip_details,
            "isp_details": isp_details,
            "request_meta": request_meta
        }

        logging.info(f"Extended Request Analysis: {analysis}")
        return JsonResponse(analysis, status=200)
    except Exception as e:
        logging.error(f"Error in extended analysis: {str(e)}")
        return JsonResponse({"error": "Internal server error."}, status=500)

# Additional functionality: Check if IP is in a blacklist
def is_ip_blacklisted(ip, blacklist):
    """Checks if the given IP address is in a predefined blacklist."""
    try:
        blacklisted = ip in blacklist
        logging.info(f"IP {ip} blacklisted: {blacklisted}")
        return blacklisted
    except Exception as e:
        logging.error(f"Error checking blacklist for IP {ip}: {str(e)}")
        return False

def analyze_request_with_blacklist(request, blacklist):
    """Analyzes a request and includes a blacklist check."""
    try:
        ip = get_client_ip(request)
        if not ip:
            return JsonResponse({"error": "Unable to determine IP address."}, status=400)

        is_blacklisted = is_ip_blacklisted(ip, blacklist)
        if is_blacklisted:
            return JsonResponse({"error": "IP address is blacklisted."}, status=403)

        ip_details = fetch_ip_details(ip)
        request_meta = get_request_meta(request)

        if not ip_details:
            return JsonResponse({
                "error": "Failed to fetch IP details.",
                "request_meta": request_meta
            }, status=500)

        analysis = {
            "ip": ip,
            "ip_details": ip_details,
            "request_meta": request_meta,
            "blacklist_check": "IP not blacklisted"
        }

        logging.info(f"Request Analysis with Blacklist: {analysis}")
        return JsonResponse(analysis, status=200)
    except Exception as e:
        logging.error(f"Error in blacklist-enhanced analysis: {str(e)}")
        return JsonResponse({"error": "Internal server error."}, status=500)

# Browser detection and filtering
def detect_browser(request):
    """Detects the browser from the User-Agent header."""
    try:
        user_agent = request.META.get("HTTP_USER_AGENT", "Unknown")
        logging.info(f"Detected browser: {user_agent}")
        return user_agent
    except Exception as e:
        logging.error(f"Error detecting browser: {str(e)}")
        return "Unknown"

def verbose_browser_info(user_agent):
    """Returns a verbose description of the browser based on the User-Agent."""
    try:
        import httpagentparser
        browser_info = httpagentparser.detect(user_agent)
        logging.info(f"Verbose browser info: {browser_info}")
        return browser_info
    except Exception as e:
        logging.error(f"Error parsing browser info: {str(e)}")
        return {"error": "Unable to parse browser info."}

def filter_browsers(request, allowed_browsers):
    """Checks if the browser is in the allowed list."""
    try:
        user_agent = detect_browser(request)
        allowed = any(browser in user_agent for browser in allowed_browsers)
        logging.info(f"Browser {user_agent} allowed: {allowed}")
        return allowed
    except Exception as e:
        logging.error(f"Error filtering browsers: {str(e)}")
        return False

def block_browsers(request, blocked_browsers):
    """Checks if the browser is in the blocked list and blocks access if so."""
    try:
        user_agent = detect_browser(request)
        blocked = any(browser in user_agent for browser in blocked_browsers)
        if blocked:
            logging.warning(f"Access blocked for browser: {user_agent}")
            return JsonResponse({"error": "Access blocked for your browser."}, status=403)
        logging.info(f"Browser {user_agent} not blocked.")
        return None
    except Exception as e:
        logging.error(f"Error blocking browsers: {str(e)}")
        return JsonResponse({"error": "Internal server error."}, status=500)
import logging
import requests
from django.http import JsonResponse
from django.utils.timezone import now

# Configure logging
logging.basicConfig(
    filename="ip_lookup.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_client_ip(request):
    """Extracts the client's IP address from the Django request object."""
    try:
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        logging.info(f"Extracted IP: {ip}")
        return ip
    except Exception as e:
        logging.error(f"Error extracting IP: {str(e)}")
        return None

def fetch_ip_details(ip):
    """Fetches detailed information about an IP address using an external API."""
    try:
        api_url = f"https://ipapi.co/{ip}/json/"
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            logging.info(f"IP Details for {ip}: {data}")
            return data
        else:
            logging.warning(f"Failed to fetch IP details for {ip}: {response.status_code}")
            return None
    except requests.RequestException as e:
        logging.error(f"Request exception for IP {ip}: {str(e)}")
        return None

def get_request_meta(request):
    """Fetches meta information from the Django request object."""
    try:
        meta_info = {
            "method": request.method,
            "path": request.path,
            "content_type": request.content_type,
            "user_agent": request.META.get("HTTP_USER_AGENT", "Unknown"),
            "referrer": request.META.get("HTTP_REFERER", "Unknown"),
            "timestamp": now().isoformat(),
        }
        logging.info(f"Request Meta: {meta_info}")
        return meta_info
    except Exception as e:
        logging.error(f"Error fetching request meta: {str(e)}")
        return {}

def get_geo_distance(ip1, ip2):
    """Calculate approximate distance between two IP locations using latitude and longitude."""
    try:
        details1 = fetch_ip_details(ip1)
        details2 = fetch_ip_details(ip2)
        if not details1 or not details2:
            return None

        from math import radians, sin, cos, sqrt, atan2

        def haversine(lat1, lon1, lat2, lon2):
            R = 6371  # Earth radius in km
            dlat = radians(lat2 - lat1)
            dlon = radians(lon2 - lon1)
            a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            return R * c

        lat1, lon1 = float(details1.get("latitude", 0)), float(details1.get("longitude", 0))
        lat2, lon2 = float(details2.get("latitude", 0)), float(details2.get("longitude", 0))

        distance = haversine(lat1, lon1, lat2, lon2)
        logging.info(f"Distance between {ip1} and {ip2}: {distance} km")
        return distance
    except Exception as e:
        logging.error(f"Error calculating distance: {str(e)}")
        return None

def analyze_request(request):
    """Analyzes a Django request and returns comprehensive details."""
    try:
        ip = get_client_ip(request)
        if not ip:
            return JsonResponse({"error": "Unable to determine IP address."}, status=400)

        ip_details = fetch_ip_details(ip)
        request_meta = get_request_meta(request)

        if not ip_details:
            return JsonResponse({
                "error": "Failed to fetch IP details.",
                "request_meta": request_meta
            }, status=500)

        analysis = {
            "ip": ip,
            "ip_details": ip_details,
            "request_meta": request_meta
        }

        logging.info(f"Request Analysis: {analysis}")
        return JsonResponse(analysis, status=200)
    except Exception as e:
        logging.error(f"Error analyzing request: {str(e)}")
        return JsonResponse({"error": "Internal server error."}, status=500)

# Sample usage in a Django view
def request_analysis_view(request):
    """Django view that analyzes the incoming request."""
    return analyze_request(request)

# Additional utility: Fetch ISP and organization details
def fetch_isp_details(ip):
    """Fetch ISP and organization details for the IP address."""
    try:
        api_url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            isp_details = {
                "isp": data.get("org", "Unknown"),
                "asn": data.get("asn", "Unknown"),
                "ip_range": data.get("range", "Unknown")
            }
            logging.info(f"ISP Details for {ip}: {isp_details}")
            return isp_details
        else:
            logging.warning(f"Failed to fetch ISP details for {ip}: {response.status_code}")
            return None
    except requests.RequestException as e:
        logging.error(f"ISP request exception for IP {ip}: {str(e)}")
        return None

# Extended analysis to include ISP details
def analyze_request_extended(request):
    """Analyzes a Django request and returns comprehensive details, including ISP."""
    try:
        ip = get_client_ip(request)
        if not ip:
            return JsonResponse({"error": "Unable to determine IP address."}, status=400)

        ip_details = fetch_ip_details(ip)
        isp_details = fetch_isp_details(ip)
        request_meta = get_request_meta(request)

        if not ip_details:
            return JsonResponse({
                "error": "Failed to fetch IP details.",
                "request_meta": request_meta
            }, status=500)

        analysis = {
            "ip": ip,
            "ip_details": ip_details,
            "isp_details": isp_details,
            "request_meta": request_meta
        }

        logging.info(f"Extended Request Analysis: {analysis}")
        return JsonResponse(analysis, status=200)
    except Exception as e:
        logging.error(f"Error in extended analysis: {str(e)}")
        return JsonResponse({"error": "Internal server error."}, status=500)

# Additional functionality: Check if IP is in a blacklist
def is_ip_blacklisted(ip, blacklist):
    """Checks if the given IP address is in a predefined blacklist."""
    try:
        blacklisted = ip in blacklist
        logging.info(f"IP {ip} blacklisted: {blacklisted}")
        return blacklisted
    except Exception as e:
        logging.error(f"Error checking blacklist for IP {ip}: {str(e)}")
        return False

def analyze_request_with_blacklist(request, blacklist):
    """Analyzes a request and includes a blacklist check."""
    try:
        ip = get_client_ip(request)
        if not ip:
            return JsonResponse({"error": "Unable to determine IP address."}, status=400)

        is_blacklisted = is_ip_blacklisted(ip, blacklist)
        if is_blacklisted:
            return JsonResponse({"error": "IP address is blacklisted."}, status=403)

        ip_details = fetch_ip_details(ip)
        request_meta = get_request_meta(request)

        if not ip_details:
            return JsonResponse({
                "error": "Failed to fetch IP details.",
                "request_meta": request_meta
            }, status=500)

        analysis = {
            "ip": ip,
            "ip_details": ip_details,
            "request_meta": request_meta,
            "blacklist_check": "IP not blacklisted"
        }

        logging.info(f"Request Analysis with Blacklist: {analysis}")
        return JsonResponse(analysis, status=200)
    except Exception as e:
        logging.error(f"Error in blacklist-enhanced analysis: {str(e)}")
        return JsonResponse({"error": "Internal server error."}, status=500)

# Browser detection and filtering
def detect_browser(request):
    """Detects the browser from the User-Agent header."""
    try:
        user_agent = request.META.get("HTTP_USER_AGENT", "Unknown")
        logging.info(f"Detected browser: {user_agent}")
        return user_agent
    except Exception as e:
        logging.error(f"Error detecting browser: {str(e)}")
        return "Unknown"

def verbose_browser_info(user_agent):
    """Returns a verbose description of the browser based on the User-Agent."""
    try:
        import httpagentparser
        browser_info = httpagentparser.detect(user_agent)
        logging.info(f"Verbose browser info: {browser_info}")
        return browser_info
    except Exception as e:
        logging.error(f"Error parsing browser info: {str(e)}")
        return {"error": "Unable to parse browser info."}

def filter_browsers(request, allowed_browsers):
    """Checks if the browser is in the allowed list."""
    try:
        user_agent = detect_browser(request)
        allowed = any(browser in user_agent for browser in allowed_browsers)
        logging.info(f"Browser {user_agent} allowed: {allowed}")
        return allowed
    except Exception as e:
        logging.error(f"Error filtering browsers: {str(e)}")
        return False

def block_browsers(request, blocked_browsers):
    """Checks if the browser is in the blocked list and blocks access if so."""
    try:
        user_agent = detect_browser(request)
        blocked = any(browser in user_agent for browser in blocked_browsers)
        if blocked:
            logging.warning(f"Access blocked for browser: {user_agent}")
            return JsonResponse({"error": "Access blocked for your browser."}, status=403)
        logging.info(f"Browser {user_agent} not blocked.")
        return None
    except Exception as e:
        logging.error(f"Error blocking browsers: {str(e)}")
        return JsonResponse({"error": "Internal server error."}, status=500)
