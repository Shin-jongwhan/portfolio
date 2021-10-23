using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TalkManager : MonoBehaviour
{
    Dictionary<int, string[]> talkData;     // 타입, 벨류
    Dictionary<int, Sprite> portraitData;

    public Sprite[] portraitArr;

    // Start is called before the first frame update
    void Awake()
    {
        talkData = new Dictionary<int, string[]>();
        portraitData = new Dictionary<int, Sprite>();
        GenerateData();
    }

    void GenerateData()
    {
        // 대화
        // NPC_A : 1000
        // NPC_B : 2000
        // Box : 100
        // Desk : 200
        talkData.Add(1000, new string[] { 
                                        "안녕?:0",      // 0, :0은 초상화를 어떤 것을 그려줄지 구분하기 위한 인덱스이다.
                                        "이 곳에 처음 왔구나?:1"      // 1
                                        });
        talkData.Add(2000, new string[] {
                                        "여어.:1",      // 0
                                        "이 호수는 정말 아름답지?:0",      // 1
                                        "사실 이 호수에는 무언가 비밀이 숨겨져 있다고 해.:1"      // 2
                                        });
        talkData.Add(100, new string[] {
                                        "평범한 나무상자다."
                                        });
        talkData.Add(200, new string[] {
                                        "누군가 사용했던 흔적이 있는 책상이다."
                                        });

        // 퀘스트 대화 1
        talkData.Add(1000 + 10, new string[] {
                                        "어서 와.:0",      // 0, :0은 초상화를 어떤 것을 그려줄지 구분하기 위한 인덱스이다.
                                        "이 마을에 놀라운 전설이 있다는데:1",      // 1
                                        "오른쪽 호수 쪽에 루도가 알려줄꺼야.:0"      // 2
                                        });
        talkData.Add(2000 + 11, new string[] {
                                        "여어.:0",      // 0
                                        "이 호수의 전설을 들으러 온거야?:1",      // 1
                                        "그럼 일 좀 하나 해주면 좋을텐데...:1",        // 2
                                        "내 집 근처에 떨어진 동전 좀 주워줬으면 해.:1"
                                        });

        // 퀘스트 대화 2
        talkData.Add(1000 + 20, new string[] {
                                        "루도의 동전?:0",      // 0
                                        "돈을 흘리고 다니면 못 쓰지!:3",      // 1
                                        "나중에 루도에게 한마디 해야겠어.:2"      // 2
                                        });
        talkData.Add(2000 + 20, new string[] {
                                        "찾으면 꼭 좀 가져다 줘.:1",      // 0
                                        });
        talkData.Add(5000 + 20, new string[] {
                                        "근처에서 동전을 찾았다.",      // 0
                                        });
        talkData.Add(2000 + 21, new string[] {
                                        "엇, 찾아줘서 고마워!:2",      // 0
                                        });


        // NPC 초상화
        portraitData.Add(1000 + 0, portraitArr[0]);
        portraitData.Add(1000 + 1, portraitArr[1]);
        portraitData.Add(1000 + 2, portraitArr[2]);
        portraitData.Add(1000 + 3, portraitArr[3]);

        portraitData.Add(2000 + 0, portraitArr[4]);
        portraitData.Add(2000 + 1, portraitArr[5]);
        portraitData.Add(2000 + 2, portraitArr[6]);
        portraitData.Add(2000 + 3, portraitArr[7]);

    }

    public string GetTalk(int id, int talkIndex)
    {
        // 퀘스트 대사 에러 처리
        if ( !talkData.ContainsKey(id))      // ContainsKey : index가 있는지 없는지 검사한다.
        {
            /*
            // 해당 퀘스트 진행 순서 중 대사가 없을 때, 퀘스트 맨 처음 대사를 가지고 온다.
            if (!talkData.ContainsKey(id - id % 10))
            {
                // 퀘스트 맨 처음 대사마저 없을 때, 기본 대사를 가지고 온다.
                if (talkIndex == talkData[id - id % 100].Length)
                    return null;
                else
                    return talkData[id - id % 100][talkIndex];
            }
            else
            {
                if (talkIndex == talkData[id - id % 10].Length)
                    return null;
                else
                    return talkData[id - id % 10][talkIndex];
                // ex) id - id%10 : (2000 + 21) - (2000 + 21) % 10 = 2021 - 1 = 2020
            }
            */

            // 코드 정리. 재귀함수를 사용할 때는 꼭 return까지 같이 써주어야 함
            if (!talkData.ContainsKey(id - id % 10))
                return GetTalk(id - id % 100, talkIndex);       // 기본 대화를 가져온다.
            else
                return GetTalk(id - id % 10, talkIndex);        // 처음 퀘스트 대화를 가져온다.
        }

        if (talkIndex == talkData[id].Length)
            return null;
        else
            return talkData[id][talkIndex];
        
    }

    public Sprite GetPortrait(int id, int portraitIndex)
    {
        return portraitData[id + portraitIndex];
    }

}
