using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class GameManager : MonoBehaviour
{
    public TalkManager talkManager;
    public QuestManager questManager;
    public Animator talkPanel;      // 처음엔 SetActive로 보였다가 사라졌다가 이렇게 했지만 애니메이터로 애니메이션 효과
    //public GameObject talkPanel;
    public Animator portraitAnim;
    public Image portraitImg;
    public Sprite previousPortrait;
    //public Text talkText;     // TypeEffect.cs 있기 전에 쓰던 것
    public TypeEffect talk;
    public Text questTalk;
    public Text TalkObjectName;
    public GameObject scanObject;
    public GameObject menuSet;
    public GameObject player;       // 게임 저장할 때 포지션 가져옴
    public bool isAction;
    public int talkIndex;

    private void Start()
    {
        GameLoad();

        //Debug.Log(questManager.CheckQuest());
        questTalk.text = questManager.CheckQuest();
    }

    private void Update()
    {
        // Sub menu
        if (Input.GetButtonDown("Cancel"))
            SubMenuActive();
    }

    public void SubMenuActive()
    {
        if (menuSet.activeSelf)
            menuSet.SetActive(false);
        else
            menuSet.SetActive(true);
    }

    public void Action(GameObject scanObj, string talkObjName)
    {
        /*
        if(isAction) {      // Exit action
            isAction = false;
        }
        else
        {       // Enter action
            isAction = true;
            talkPanel.SetActive(true);
            scanObject = scanObj;
            //talkText.text = "이것의 이름은 " + scanObject.name + "이라고 한다.";

            ObjData objData = scanObject.GetComponent<ObjData>();
            Talk(objData.id, objData.inNpc);
        }
        */

        scanObject = scanObj;
        TalkObjectName.text = talkObjName;
        ObjData objData = scanObject.GetComponent<ObjData>();
        Talk(objData.id, objData.isNpc);

        // Talk(objData.id, objData.isNpc);에서 가져온 isAction으로 true, false 입력
        //talkPanel.SetActive(isAction);
        talkPanel.SetBool("isShow", isAction);
    }

    void Talk(int id, bool isNpc)
    {
        // Set talk data
        int questTalkIndex = 0;
        string talkData = "";

        if (talk.isAnim)
        {
            talk.SetMsg("");
            return;
        }
        else
        {
            questTalkIndex = questManager.GetQuestTalkIndex(id);
            talkData = talkManager.GetTalk(id + questTalkIndex, talkIndex);
        }

        // End talk
        if (talkData == null)
        {
            isAction = false;
            talkIndex = 0;
            questTalk.text = questManager.CheckQuest(id);
            //Debug.Log(questManager.CheckQuest(id));
            return;     // void 함수에서는 return 뒤에 아무 것도 안 쓰고 return 써주면 됨.
        }

        // Continue talk
        if (isNpc)
        {
            talk.SetMsg(talkData.Split(':')[0]);

            // Show portrait
            portraitImg.sprite = talkManager.GetPortrait(id, int.Parse(talkData.Split(':')[1]));        // int.Parse : 문자열 타입을 int 타입으로 형변환
            portraitImg.color = new Color(1, 1, 1, 1);      // 1,1,1,1의 4번째 값 : 알파값(투명도)
            // Animation portrait
            if (portraitImg != previousPortrait)
            {
                portraitAnim.SetTrigger("doEffect");
                previousPortrait = portraitImg.sprite;
            }
        }
        else
        {
            talk.SetMsg(talkData);

            portraitImg.color = new Color(1, 1, 1, 0);      // NPC일 때만 Image가 보이도록 함
        }

        isAction = true;
        talkIndex++;

    }

    public void GameSave()
    {
        // 레지스트리에 Player의 x, y positin, QuestId, QuestActionIndex를 각각의 명칭으로 저장한다.
        PlayerPrefs.SetFloat("PlayerX", player.transform.position.x);
        PlayerPrefs.SetFloat("PlayerY", player.transform.position.y);
        PlayerPrefs.SetInt("QuestId", questManager.questId);
        PlayerPrefs.SetInt("QuestActionIndex", questManager.questActionIndex);
        PlayerPrefs.Save();

        menuSet.SetActive(false);
    }

    public void GameLoad()
    {
        if (!PlayerPrefs.HasKey("PlayerX"))
        {
            return;
        }
        float x = PlayerPrefs.GetFloat("PlayerX");
        float y = PlayerPrefs.GetFloat("PlayerY");
        int questId = PlayerPrefs.GetInt("QuestId");
        int QuestActionIndex = PlayerPrefs.GetInt("QuestActionIndex");

        player.transform.position = new Vector3(x, y, 0);
        questManager.questId = questId;
        questManager.questActionIndex = QuestActionIndex;
        questManager.ControlObject();
    }

    public void GameExit()
    {
        //DeletePlayerPrefs();
        Application.Quit();
    }

    static void DeletePlayerPrefs()     // 유니티 엔진에서 실행할 때만 이용
    {
        PlayerPrefs.DeleteAll();
        Debug.Log("All PlayerPrefs deleted");
    }

}
