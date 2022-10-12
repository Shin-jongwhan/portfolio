using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TypeEffect : MonoBehaviour
{
    public GameObject endCursor;
    public int charPerSeconds;
    public bool isAnim;

    Text msgText;
    AudioSource audioSource;

    string targetMassage;
    int index;
    float interval;

    private void Awake()
    {
        msgText = GetComponent<Text>();
        audioSource = GetComponent<AudioSource>();
    }

    public void SetMsg(string msg)
    {
        if (isAnim)     // Interrupt
        {
            msgText.text = targetMassage;
            CancelInvoke();     // Invoke �Լ��� ����.
            EffectEnd();
        }
        else {
            targetMassage = msg;
            EffectStart();
        }
    }

    void EffectStart()
    {
        msgText.text = "";
        index = 0;
        endCursor.SetActive(false);

        interval = 1.0f / charPerSeconds;
        //Debug.Log(interval);

        isAnim = true;

        Invoke("Effecting", interval);        // 1�ʿ� �� �� type�ǰ� �� ������
    }

    void Effecting()
    {
        if (msgText.text == targetMassage)      // text�� �������� �Ǹ� return�Ͽ� ������.
        {
            EffectEnd();
            return;
        }

        msgText.text += targetMassage[index];
        
        if (targetMassage[index] != ' ' || targetMassage[index] != '.')
        {
            audioSource.Play();
        }
        index++;

        Invoke("Effecting", interval);
    }

    void EffectEnd()
    {
        endCursor.SetActive(true);
        isAnim = false;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
