using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class QuestManager : MonoBehaviour
{
    public int questId;
    public int questActionIndex;        // 대화 순서 설정
    public GameObject[] questObject;

    Dictionary<int, QuestData> questList;


    // Start is called before the first frame update
    void Awake()
    {
        questList = new Dictionary<int, QuestData>();
        GenerateData();
    }

    void GenerateData()
    {
        questList.Add(10, new QuestData("마음 사람들과 대화하기.", 
                                        new int[] { 1000, 2000 }));
        questList.Add(20, new QuestData("루도의 동전 찾아주기.",
                                        new int[] { 5000, 2000 }));
        questList.Add(30, new QuestData("퀘스트 올 클리어!",
                                        new int[] { 0 }));
    }

    public int GetQuestTalkIndex(int id)        // NPC id를 받고 퀘스트 번호를 반환하는 함수 생성
    {
        return questId + questActionIndex;
    }

    public string CheckQuest(int id)
    {
        // Talk next target
        if (id == questList[questId].npcId[questActionIndex])
            questActionIndex++;

        // Control quest object
        ControlObject();

        // Talk complete & Next quest
        if (questActionIndex == questList[questId].npcId.Length)
            NextQuest();

        // Quest name
        return questList[questId].questName;
    }

    public string CheckQuest()      // 오버로딩 : 매개변수에 따라 함수를 호출
    {
        // Quest name
        return questList[questId].questName;
    }

    void NextQuest()
    {
        questId += 10;
        questActionIndex = 0;
    }
    public void ControlObject()
    {
        switch (questId)
        {
            case 10:
                if (questActionIndex == 2)
                {
                    questObject[0].SetActive(true);
                }
                break;
            case 20:
                if (questActionIndex == 0)
                {
                    questObject[0].SetActive(true);
                }
                if (questActionIndex == 1)
                {
                    questObject[0].SetActive(false);
                }
                break;
        }
    }

}
