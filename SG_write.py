#テスト段階
# path = r'C:\Users\y-yoshioka\Desktop\test.txt'
# s ="lplplplpp"
# try:
#     f = open(path)
#     with open(path, mode='w') as f:
#         f.write(s)
#     f.close()
# except FileExistsError:
#     pass

import sys

P=r"C:\Users\y-yoshioka\AppData\Roaming\Python\Python310\site-packages"
PP =r"C:\Users\y-yoshioka\AppData\Local\Programs\Python\Python310\Lib\site-packages"
sys.path.append(P)
sys.path.append(PP)
# for i in sys.path:
#     print(i)


from shotgun_api3 import Shotgun

def createSG_API():
    sg = Shotgun(
    "https://aaaaa.shotgrid.autodesk.com",
    script_name="BlenderFileUpload_test",
    api_key="hogehoge"
    )
    return sg
def setData():
    data = {
    "project": {"type": "Project", "id": 122},
    "sg_sequence": {"type": "Sequence", "id": 74},
    "code": "B31_EP11_888",
    "sg_status_list": "wtg",
    "sg_cut_duration":7777
    }
    return data


def main():
   shotgun_api = createSG_API()
#   ShotをB31に登録する
   shotgun_api.create('Shot', setData())
   return 0

if __name__ == "__main__":
   main()
