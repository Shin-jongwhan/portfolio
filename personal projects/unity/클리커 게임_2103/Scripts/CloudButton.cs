using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CloudButton : MonoBehaviour
{
    public void LoadGold()
    {
        // LoadFromCloud( () => {} )
        // () : 입력, {} : 바디. 입력으로 데이터를 받아서 바디에 저장
        //long.Parse : 문장에서 숫자로 바꿔주는 것.
        PlayCloudDataManager.Instance.LoadFromCloud((string dataToLoad) => { DataController.Instance.gold = long.Parse(dataToLoad); });
    }

    public void SaveGold()
    {
        PlayCloudDataManager.Instance.SaveToCloud(DataController.Instance.gold.ToString());
    }


}
