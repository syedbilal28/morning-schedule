from flask import Flask,render_template,json,request

app= Flask(__name__)

@app.route("/")
def index():
    infile= open("schedule.txt","r")
    data = infile.readlines()
    infile.close()
    infile=open("traveltime.txt","r")
    travel_time= infile.read()
    travel_time=travel_time.strip().split(",")
    traveltimehours,traveltimemins= travel_time[0],travel_time[1]

    l= len(data)
    for i in range(l):
        data[i]=data[i].replace("\n","")
    print(data)
    # context={"data":data}
    return render_template("index.html",data=data,travelhours=traveltimehours,travelmins=traveltimemins)
 
@app.route("/changedata",methods=["POST","GET"])
def changedata():
    json_data=request.get_json("")
    
    pk= json_data["pk"]
    value=json_data["data"]
    infile= open("schedule.txt","r")
    data = infile.readlines()
    infile.close()
    print(data,"here")
    l= len(data)
    for i in range(l):
        data[i]=data[i].replace("\n","")
    data[int(pk)-1]=value
    outfile= open("schedule.txt","w")
    for i in data:
        outfile.write(f"{str(i)}\n")
    response = app.response_class(
        response=json.dumps({"message":"Changed"}),
        status=200,
        mimetype='application/json'
    )
    return response