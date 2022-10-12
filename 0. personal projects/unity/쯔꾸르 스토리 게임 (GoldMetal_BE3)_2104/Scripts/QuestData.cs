using System.Collections;
using System.Collections.Generic;

public class QuestData
{
    public string questName;
    public int[] npcId;

    public QuestData(string name, int[] npc)     // 클래스의 생성자. 다른 스크립트에서 파라미터 받고 싶을 때 이렇게 쓰면 된다.
    {
        questName = name;
        npcId = npc;
    }
}
