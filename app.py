from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

allowed_friend_keys = ("GAY_hack", "BERLIN", "HACK")

spam_visit_key = ("GAY_hack", "HACK")

allowed_like_key = {
    "GAY_hack": "https://like-krishna-kd23.vercel.app",
    "BERLIN": "https://like-gs3q.vercel.app",
    "HACK": "https://likess.vercel.app"
}

allowed_keys = ("GAY_hack", "BERLIN", "HACK")

@app.route("/profile_info", methods=["GET"])
def profile_info():
    uid = request.args.get("uid")
    region = request.args.get("region")
    key = request.args.get("key")
    
    if not uid or not region or not key:
        return jsonify({'error': 'uid, region, and key are required'}), 400
    
    if key in allowed_keys:
        response = requests.get(f"https://profile-info-ten.vercel.app/profile_info?uid={uid}&region={region}")
        if response.status_code == 200:
            try:
                data = response.json()
                return jsonify(data), 200
            except ValueError:
                return jsonify({"error": "Invalid JSON response from the server"}), 500
        else:
            return jsonify({"error": "Something went wrong. Please check your UID and Region."}), response.status_code
    else:
        return jsonify({'error': "Invalid Key. Please check your key."}), 403
        
@app.route("/guild_info", methods=["GET"])
def guild_info():
    clanid = request.args.get("clanid")
    region = request.args.get("region")
    key = request.args.get("key")
    
    if not clanid or not region or not key:
        return jsonify({'error': 'ClanID, region, and key are required'}), 400
    
    if key in allowed_keys:
        response = requests.get(f"https://guild-info-sigma.vercel.app/guild_info?clan_id={clanid}&region={region}")
        if response.status_code == 200:
            return response.text
        else:
            return jsonify({"error": "Something went wrong. Please check your ClanID and Region."}), response.status_code
    else:
        return jsonify({'error': "Invalid Key. Please check your key."}), 403
        
@app.route("/wishlist_info", methods=["GET"])
def wishlist_info():
    uid = request.args.get("uid")
    region = request.args.get("region")
    key = request.args.get("key")
    
    if not uid or not region or not key:
        return jsonify({'error': 'uid, region, and key are required'}), 400
    
    if key in allowed_keys:
        response = requests.get(f"https://wishlist-info.vercel.app/wishlist_info?uid={uid}&region={region}")
        if response.status_code == 200:
            return response.text
        else:
            return jsonify({"error": "Something went wrong. Please check your UID and Region."}), response.status_code
    else:
        return jsonify({'error': "Invalid Key. Please check your key."}), 403
        
@app.route("/banner_info", methods=["GET"])
def banner_info():
    region = request.args.get("region")
    key = request.args.get("key")
    
    if not region or not key:
        return jsonify({'error': 'region and key are required'}), 400
    
    if key in allowed_keys:
        response = requests.get(f"https://banner-api.vercel.app/banner?region={region}")
        if response.status_code == 200:
            return response.text
        else:
            return jsonify({"error": "Something went wrong. Please check your Region."}), response.status_code
    else:
        return jsonify({'error': "Invalid Key. Please check your key."}), 403

@app.route("/region_info", methods=["GET"])
def region_info():
    uid = request.args.get("uid")
    key = request.args.get("key")
    
    if not uid or not key:
        return jsonify({'error': 'uid and key are required'}), 400
    
    if key in allowed_keys:
        response = requests.get(f"https://region-infokrishna.vercel.app/region_info?uid={uid}")
        if response.status_code == 200:
            return response.text
        else:
            return jsonify({"error": "Something went wrong. Please check your UID."}), response.status_code
    else:
        return jsonify({'error': "Invalid Key. Please check your key."}), 403

@app.route("/check_banned", methods=["GET"])
def check_banned():
    uid = request.args.get("uid")
    key = request.args.get("key")
    
    if not uid or not key:
        return jsonify({'error': 'uid and key are required'}), 400
    
    if key in allowed_keys:
        response = requests.get(f"https://check-banned-krishna.vercel.app/check_banned/{uid}")
        if response.status_code == 200:
            return response.text
        else:
            return jsonify({"error": "Something went wrong. Please check your UID."}), response.status_code
    else:
        return jsonify({'error': "Invalid Key. Please check your key."}), 403

@app.route("/jwtinfo", methods=["GET"])
def jwtinfo():
    uid = request.args.get("uid")
    password = request.args.get("password")
    key = request.args.get("key")
    
    if not uid or not password or not key:
        return jsonify({'error': 'uid, password and key are required'}), 400
    
    if key in allowed_keys:
        response = requests.get(f"https://jwtinfo-api.vercel.app/{uid}/{password}")
        if response.status_code == 200:
            return response.text
        else:
            return jsonify({"error": "Something went wrong. Please check your UID And Password."}), response.status_code
    else:
        return jsonify({'error': "Invalid Key. Please check your key."}), 403

@app.route("/jwt", methods=["GET"])
def jwt():
    region = request.args.get("region")
    key = request.args.get("key")
    
    if not region or not key:
        return jsonify({'error': 'region and key are required'}), 400
    
    if key in allowed_keys:
        response = requests.get(f"https://krishna-get-token.vercel.app/token?region={region}")
        if response.status_code == 200:
            return response.text
        else:
            return jsonify({"error": "Something went wrong. Please check your UID And Password."}), response.status_code
    else:
        return jsonify({'error': "Invalid Key. Please check your key."}), 403

@app.route("/spam_visit", methods=["GET"])
def spam_visit():
    uid = request.args.get("uid")
    region = request.args.get("region")
    key = request.args.get("key")
    
    if not region or not key:
        return jsonify({'error': 'uid, region and key are required'}), 400
    
    if key in spam_visit_key:
        response = requests.get(f"https://visits-psi.vercel.app/send_requests?uid={uid}&server_name={region}")
        if response.status_code == 200:
            return jsonify({'status': response.text}), 200
        else:
            return jsonify({"error": "Something went wrong. Please check your UID And Region."}), response.status_code
    else:
        return jsonify({'error': "Invalid Key. Please check your key."}), 403

@app.route("/like_profile", methods=["GET"])
def like_profile():
    uid = request.args.get("uid")
    region = request.args.get("region")
    key = request.args.get("key")
    
    if not uid or not region or not key:
        return jsonify({'error': 'uid, region, and key are required'}), 400

    if key in allowed_like_key:
        url = allowed_like_key[key]

        try:
            response = requests.get(f"{url}/like?uid={uid}&server_name={region}")
        except requests.RequestException as e:
            return jsonify({"error": "Failed to connect to the like service.", "details": str(e)}), 500

        if response.status_code == 200:
            try:
                data = response.json()
                result = {
                    "response": {
                        "LikesGivenByAPI": data.get("LikesGivenByAPI", 0),
                        "LikesafterCommand": data.get("LikesafterCommand", 0),
                        "LikesbeforeCommand": data.get("LikesbeforeCommand", 0),
                        "PlayerNickname": data.get("PlayerNickname", ""),
                        "UID": data.get("UID", "")
                    },
                    "status": data.get("status", "Unknown")
                }
                return jsonify(result), 200
            except ValueError:
                return jsonify({"error": "Invalid JSON response from the like service."}), 500
        else:
            return jsonify({"error": "Something went wrong. Please check your UID and Region."}), response.status_code
    else:
        return jsonify({'error': "Invalid Key. Please check your key."}), 403
        
@app.route("/spam_request", methods=["GET"])
def spam_request():
    uid = request.args.get("uid")
    region = request.args.get("region")
    key = request.args.get("key")
    
    if not region or not key:
        return jsonify({'error': 'uid, region and key are required'}), 400
    
    if key in allowed_friend_keys:
        response = requests.get(f"https://request-eight.vercel.app/spam_request?uid={uid}&server_name={region}")
        if response.status_code == 200:
            return jsonify({'status': response.text}), 200
        else:
            return jsonify({"error": "Something went wrong. Please check your UID And Region."}), response.status_code
    else:
        return jsonify({'error': "Invalid Key. Please check your key."}), 403

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': "Invalid Request. Please check your URL."}), 404


if __name__ == "__main__":
    app.run(debug=True)
