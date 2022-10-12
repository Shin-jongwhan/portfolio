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
            CancelInvoke();     // Invoke 함수를 끈다.
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

        Invoke("Effecting", interval);        // 1초에 몇 번 type되게 할 것인지
    }

    void Effecting()
    {
        if (msgText.text == targetMassage)      // text가 마지막이 되면 return하여 끝낸다.
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
