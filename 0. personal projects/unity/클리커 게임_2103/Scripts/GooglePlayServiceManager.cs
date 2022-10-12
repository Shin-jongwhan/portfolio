using System.Collections;
using System.Collections.Generic;
using UnityEngine;

using GooglePlayGames;
using GooglePlayGames.BasicApi;
using UnityEngine.SocialPlatforms;

public class GooglePlayServiceManager : MonoBehaviour
{
    static private GooglePlayServiceManager instance;

    public static GooglePlayServiceManager Instance
    {
        get
        {
            if (instance == null)
            {
                instance = FindObjectOfType<GooglePlayServiceManager>();

                if(instance == null)
                {
                    instance = new GameObject("Google Play Service").AddComponent<GooglePlayServiceManager>();
                }
            }

            return instance;
        }
    }



    // Start is called before the first frame update
    void Awake()
    {
        //Builder() : . ~~~ .Build(); 안에 있는 함수를 같이 실행시켜 주고 Build()함수를 실행시킨다.
        PlayGamesClientConfiguration config = new PlayGamesClientConfiguration.Builder().EnableSavedGames().Build();

        PlayGamesPlatform.InitializeInstance(config);

        PlayGamesPlatform.DebugLogEnabled = false;

        PlayGamesPlatform.Activate();
    }

    public void Login()
    {
        Social.localUser.Authenticate( (bool success) => { if (!success) { Debug.Log("Login Fail"); } } );
    }

    public bool isAuthenticated
    {
        //로그인이 되었는지 안 되었는지 확인
        get
        {
            return Social.localUser.authenticated;
        }
    }

    public void CompleteFirstLogin()
    {
        if (!isAuthenticated)
        {
            Login();    //아직 로그인 안 되었다면 로그인 다시 시도
            return;
        }
        //100.0 : 0이면 수행하지 못한 것, 100이면 완성한 것
        Social.ReportProgress(GPGSIds.achievement, 100.0, (bool success) => { if (!success) { Debug.Log("Report Fail!"); } } );
    }

    public void Complete1000Gold()
    {
        if (!isAuthenticated)
        {
            Login();
            return;
        }
        Social.ReportProgress(GPGSIds.achievement_1000, 100.0, (bool success) => {if(success) {PlayerPrefs.SetInt("Complete1000Gold", 1); } } );
    }

    public void ShowAchievementUI()
    {
        if (!isAuthenticated)
        {
            Login();
            return;
        }
        Social.ShowAchievementsUI();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
