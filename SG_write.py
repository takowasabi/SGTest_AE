


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
