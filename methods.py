marks={
    "subject":{
        "programming language":{
            "python":80,
            "java":99,
            "c++":90,
        }
    },
    "coders":{
        "ritu":"python",
        "tanu":"c++",
        "tiya":"java"
    }
}
print(marks)
marks.keys()#return all keys in marks
marks.values()#returns all values in marks
marks.items()#returns all items in marks
marks.get("key")#returns the key according to the value
marks.update({"pass":"above 50","fail":"below 50"})
print(type(marks))
marks.clear()#clear all the items in the marks
marks.copy()#returns a copy of the marks
print(marks)