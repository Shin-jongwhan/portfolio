/*
PlauerPrefs는 GetInt와 SetInt가 있다.
PlauerPrefs : 로컬에 KEY : VALUE로 데이터를 저장함
get을 해주면 KEY 값에 맞는 VALUE를 불러옴
set을 해주면 KEY 값에 맞는 VALUE를 저장
key 값이 존재하지 않으면 0으로 저장
*/
//m_goldPerClick을 저장한 GoldPerClick으로 값을 불러온다.
//m_goldPerClick은 0이지만 값이 존재하지 않을 때는 1로 불러온다.

//Find'Objects'OfType: 이름에 맞는 모든 오브젝트들을 가져온다
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;   //시간을 가져오고 저장하기 위해 쓰임
using System.Text;
using UnityEngine.UI;

public class DataController : MonoBehaviour 
{
    //public DataController dataController를 선언하고
    //instance를 이용해서 inspector 안에서 추가해주는 것이 아닌 
    //바로 추가해주게 함
    private static DataController instance;

    public static DataController Instance   // return instance기능을 가진 Instance 변수로써 접근
    {
        // Instance에선 프로퍼티로 사용할 때 get만 만든다.
        // ~ = Instance와 같이 외부에서 get으로 가져올 수는 있지만
        // Instance = ~와 같이 Instance를 임의로 조정가능하지 못하게 set은 작성 X
        get
        {
            if (instance == null)    //instance가 아직 할당이 안 되었다면
            {
                //해당 타입에 맞는 걸 Scene에 있는 모든 오브젝트를 뒤져서
                //DataController를 찾아서 넣어준다.
                instance = FindObjectOfType<DataController>();

                if (instance == null)   //찾아봤는데도 없다면
                {
                    //빈 GameObject를 하나 만듦
                    //container라는 거에 GameObject를 단순하게 담을 것을 지정
                    //GameObject 이름은 DataController
                    GameObject container = new GameObject("DataController");
                    //AddComponent를 통해서 DataController를 붙혀줌
                    instance = container.AddComponent<DataController>();
                }
            }
            return instance;
        }
    }

    //public Text connectionReward;
    //public CanvasGroup reward_canvasGroup;

    private ItemButton[] itemButtons;   //scene에 존재하는 모든 itemButton을 다 가져와서 배열에 저장
    //그런 다음 goldPerSec을 가져와서 합산

    DateTime GetLastPlayDate()
    {
        if (!PlayerPrefs.HasKey("Time"))
        {
            return DateTime.Now;
        }

        string timeBinaryInString = PlayerPrefs.GetString("Time");
        long timeBinaryInLong = Convert.ToInt64(timeBinaryInString);

        return DateTime.FromBinary(timeBinaryInLong);
    }

    public void UpdateLastPlayDate()
    {
        //마지막으로 플레이한 시간 저장
        PlayerPrefs.SetString("Time", DateTime.Now.ToBinary().ToString());
    }

    private void OnApplicationQuit()    //게임을 종료하기 직전 자동적으로 실행되는 함수
    {
        UpdateLastPlayDate();
    }

    //gold = 30; 이라고 했을 떄 이건 m_gold안의 set이 동작해서 value에 30을 짚어넣어준 것으로 내부에서 처리함
    //a = gold; 이면 get으로 들어가서 동작함
    //게임을 다시 시작할 때 로드해주는 기능
    public long gold
    {
        get
        {
            //문장으로 저장하여 long으로 변환하면 int형을 받는 GetInt의 문제점을 잡을 수 있다
            if (! PlayerPrefs.HasKey("Gold"))
            {
                /*
                string tmpGold = PlayerPrefs.GetString("Gold");에서 저장된 "Gold"가 없다면 빈 문장을 가져다주는데
                return long.Parse(tmpGold);에서 빈문장을 받으면 에러가 난다
                이를 해결하기 위해 HasKey("Gold")를 해서 저장을 한게 없다면 return 0;
                */
                return 0;
            }
            string tmpGold = PlayerPrefs.GetString("Gold");
            return long.Parse(tmpGold);
        }
        set
        {
            if( value > 1000 && !PlayerPrefs.HasKey("Achievement_1000"))
            {
                // 1000골드 이상이고 Achievement_1000 prefs가 없다면 완수
                GooglePlayServiceManager.Instance.Complete1000Gold();
            }
            PlayerPrefs.SetString("Gold", value.ToString());
        }
    }
    public int goldPerClick
    {
        get
        {
            return PlayerPrefs.GetInt("GoldPerClick", 1);
        }
        set
        {
            PlayerPrefs.SetInt("GoldPerClick", value);
        }
    }

    public int timeAfterLastPlay    //게임 종료 후 다시 게임을 켠 시간
    {
        get
        {
            DateTime currentTime = DateTime.Now;
            DateTime lastPlayDate = GetLastPlayDate();
            //currentTime에서 lastPlayDate만큼 빼준 시간을 초단위로 return
            return (int) currentTime.Subtract(lastPlayDate).TotalSeconds;
        }
    }

    void Awake()
    {
        //게임이 처음 시작할 때 실행되는 함수
        //로컬에다가 데이터를 저장해놓고 필요할 때마다 꺼내쓰게 함
        //PlayerPrefs.DeleteAll();
        itemButtons = FindObjectsOfType<ItemButton>();

        GooglePlayServiceManager.Instance.Login();  // 게임이 시작되면 로그인 창이 뜸
    }

    private void Start()
    {
        //게임 종료하고 다시 돌아올 때 보너스로 주는 gold
        gold += GetGoldPerSec() * timeAfterLastPlay;
        //UpdateLastPlayDate라는 함수를 0초에 시작해서 5초마다 반복 실행해줌
        InvokeRepeating("UpdateLastPlayDate", 0f, 5f);

        Invoke("CompleteFirstLoginWrapper", 10f);   //CompleteFirstLoginWrapper라는 함수를 10초 뒤 실행한다.

        /*
        if(GetGoldPerSec() * timeAfterLastPlay != 0)
        {
            reward_canvasGroup.alpha = 1.0f;
            connectionReward.text = "미접속 보상!\n" + GetGoldPerSec() * timeAfterLastPlay;
        }
        */
    }

    private void CompleteFirstLoginWrapper()
    {
        // Start()에 Invoke() 라는 함수를 통해 지연시간을 줘서 first login 도전 과제가 첫 로그인시 완수될 수 있도록 함
        if (GooglePlayServiceManager.Instance.isAuthenticated)
        {
            //로그인 인증하고 두번째 로그인 때 완수
            GooglePlayServiceManager.Instance.CompleteFirstLogin();
        }
    }

    //업그레이드 버튼을 로드 (게임을 끄고 다시 시작해도 이전에 업그레이드 해놨던 단계에서 시작하게끔)
    public void LoadUpgradeButton(UpgradeButton upgradeButton)
    {
        string key = upgradeButton.upgradeName;

        //만약에 값을 찾지 못하면 1을 대신 넣어라
        upgradeButton.level = PlayerPrefs.GetInt(key + "_level", 1);
        upgradeButton.goldByUpgrade = PlayerPrefs.GetInt(key + "_goldByUpgrade", upgradeButton.startGoldByUpgrade);
        upgradeButton.currentCost = PlayerPrefs.GetInt(key + "_cost", upgradeButton.startCurrentCost);
    }

    //업그레이드 버튼을 저장
    public void SaveUpgradeButton(UpgradeButton upgradeButton)
    {
        string key = upgradeButton.upgradeName;

        //만약에 값을 찾지 못하면 1을 대신 넣어라
        PlayerPrefs.SetInt(key + "_level", upgradeButton.level);
        PlayerPrefs.SetInt(key + "_goldByUpgrade", upgradeButton.goldByUpgrade);
        PlayerPrefs.SetInt(key + "_cost", upgradeButton.currentCost);
    }

    public void LoadItemButton(ItemButton itemButton)
    {
        string key = itemButton.itemName;

        itemButton.level = PlayerPrefs.GetInt(key + "_level");
        itemButton.currentCost = PlayerPrefs.GetInt(key + "_cost", itemButton.startCurrentCost);
        itemButton.goldPerSec = PlayerPrefs.GetInt(key + "_goldPerSec");

        //PlayerPrefs는 Genint는 있지만 GetBool은 없기 때문에 true == 1, flase == 0
        if( PlayerPrefs.GetInt(key + "_isPurchased") == 1)
        {
            itemButton.isPurchased = true;
        }
        else  // 1아니면 0
        {
            itemButton.isPurchased = false;
        }
    }

    public void SaveItemButton(ItemButton itemButton)
    {
        string key = itemButton.itemName;

        PlayerPrefs.SetInt(key + "_level", itemButton.level);
        PlayerPrefs.SetInt(key + "_cost", itemButton.currentCost);
        PlayerPrefs.SetInt(key + "_goldPerSec", itemButton.goldPerSec);

        //PlayerPrefs는 Genint는 있지만 GetBool은 없기 때문에 true인지 false인지 따로 구분해줘야 한다.
        if (itemButton.isPurchased == true)
        {
            PlayerPrefs.SetInt(key + "_isPurchased", 1);
        }
        else  // false이면 0
        {
            PlayerPrefs.SetInt(key + "_isPurchased", 0);
        }
    }

    public int GetGoldPerSec()
    {
        int goldPerSec = 0;
        for(int i = 0; i < itemButtons.Length; i++) //Length : 배열의 개수
        {
            if (itemButtons[i].isPurchased == true)
                goldPerSec += itemButtons[i].goldPerSec;
        }

        return goldPerSec;
    }
}
