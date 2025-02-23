from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = 'INTERNSHIPtspmo' #replace verify_token string with suitable string. 
                                 #make sure string is inputted exactly into meta webhook verification section

@app.route('/webhook', methods=['GET','POST'])
def callback_handler():
    if request.method == 'GET':
        hub_mode = request.args.get("hub.mode")
        hub_challenge = request.args.get("hub.challenge")
        hub_token = request.args.get("hub.verify_token")

        # for debugging purposeses
        print(f"hub.mode: {hub_mode}")
        print(f"hub.challenge: {hub_challenge}")
        print(f"hub.verify_token: {hub_token}")

        if hub_token == VERIFY_TOKEN and hub_mode=='subscribe':
            print(f"Verification successful! Returning hub.challenge: {hub_challenge}")
            return hub_challenge    #returns the string back to Meta's server
        else:
            print("ts failed ngl")
            return "Verification failed", 403  # 403 error code

    elif request.method=='POST':
        data = request.json
        print("Webhook received:", data)
        return "Event received", 200 
    
    

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    #runs on port 8080
    #usage: python <filename>.py

