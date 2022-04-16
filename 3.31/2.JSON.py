j_data2={
    "key1":"data1",
    "key2":"data2",
    "key3":"data3",
    "key4":"data"
}
j_data1={
    "key4":"data1",
    "key5":"data2",
    "key6":"data3",
    "key7":[j_data2,j_data2]
}
#
import json
with open("data.json",'w') as f: #json 문자열기반이기때문에 피클바이너리사용x
    json.dump(j_data1,f)
    #json.dump(j_data2,f)

