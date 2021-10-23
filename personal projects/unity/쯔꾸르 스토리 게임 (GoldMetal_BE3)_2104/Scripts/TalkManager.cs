using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TalkManager : MonoBehaviour
{
    Dictionary<int, string[]> talkData;     // Ÿ��, ����
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
        // ��ȭ
        // NPC_A : 1000
        // NPC_B : 2000
        // Box : 100
        // Desk : 200
        talkData.Add(1000, new string[] { 
                                        "�ȳ�?:0",      // 0, :0�� �ʻ�ȭ�� � ���� �׷����� �����ϱ� ���� �ε����̴�.
                                        "�� ���� ó�� �Ա���?:1"      // 1
                                        });
        talkData.Add(2000, new string[] {
                                        "����.:1",      // 0
                                        "�� ȣ���� ���� �Ƹ�����?:0",      // 1
                                        "��� �� ȣ������ ���� ����� ������ �ִٰ� ��.:1"      // 2
                                        });
        talkData.Add(100, new string[] {
                                        "����� �������ڴ�."
                                        });
        talkData.Add(200, new string[] {
                                        "������ ����ߴ� ������ �ִ� å���̴�."
                                        });

        // ����Ʈ ��ȭ 1
        talkData.Add(1000 + 10, new string[] {
                                        "� ��.:0",      // 0, :0�� �ʻ�ȭ�� � ���� �׷����� �����ϱ� ���� �ε����̴�.
                                        "�� ������ ���� ������ �ִٴµ�:1",      // 1
                                        "������ ȣ�� �ʿ� �絵�� �˷��ٲ���.:0"      // 2
                                        });
        talkData.Add(2000 + 11, new string[] {
                                        "����.:0",      // 0
                                        "�� ȣ���� ������ ������ �°ž�?:1",      // 1
                                        "�׷� �� �� �ϳ� ���ָ� �����ٵ�...:1",        // 2
                                        "�� �� ��ó�� ������ ���� �� �ֿ������� ��.:1"
                                        });

        // ����Ʈ ��ȭ 2
        talkData.Add(1000 + 20, new string[] {
                                        "�絵�� ����?:0",      // 0
                                        "���� �긮�� �ٴϸ� �� ����!:3",      // 1
                                        "���߿� �絵���� �Ѹ��� �ؾ߰ھ�.:2"      // 2
                                        });
        talkData.Add(2000 + 20, new string[] {
                                        "ã���� �� �� ������ ��.:1",      // 0
                                        });
        talkData.Add(5000 + 20, new string[] {
                                        "��ó���� ������ ã�Ҵ�.",      // 0
                                        });
        talkData.Add(2000 + 21, new string[] {
                                        "��, ã���༭ ����!:2",      // 0
                                        });


        // NPC �ʻ�ȭ
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
        // ����Ʈ ��� ���� ó��
        if ( !talkData.ContainsKey(id))      // ContainsKey : index�� �ִ��� ������ �˻��Ѵ�.
        {
            /*
            // �ش� ����Ʈ ���� ���� �� ��簡 ���� ��, ����Ʈ �� ó�� ��縦 ������ �´�.
            if (!talkData.ContainsKey(id - id % 10))
            {
                // ����Ʈ �� ó�� ��縶�� ���� ��, �⺻ ��縦 ������ �´�.
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

            // �ڵ� ����. ����Լ��� ����� ���� �� return���� ���� ���־�� ��
            if (!talkData.ContainsKey(id - id % 10))
                return GetTalk(id - id % 100, talkIndex);       // �⺻ ��ȭ�� �����´�.
            else
                return GetTalk(id - id % 10, talkIndex);        // ó�� ����Ʈ ��ȭ�� �����´�.
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
