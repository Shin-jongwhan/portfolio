using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class PlayerBall : MonoBehaviour
{
    public float jumpPower = 10f;
    public int itemCount;
    public GameManagerLogic manager;
    bool isJump;
    Rigidbody rigid;
    AudioSource audio;

    private void Awake()
    {
        isJump = false;
        rigid = GetComponent<Rigidbody>();
        audio = GetComponent<AudioSource>();
    }

    private void Update()
    {
        if (Input.GetButtonDown("Jump") && !isJump)
        {
            isJump = true;
            rigid.AddForce(new Vector3(0, jumpPower, 0), ForceMode.Impulse);
        }
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        float h = Input.GetAxisRaw("Horizontal");
        float v = Input.GetAxisRaw("Vertical");

        rigid.AddForce(new Vector3(h, 0, v), ForceMode.Impulse);
        //Debug.Log(rigid.velocity);

        if (transform.position.y < -10)
        {
            SceneManager.LoadScene(manager.stage);      // build setting에서 scene 번호 인덱스를 볼 수 있는데, 인덱스를 적어줘도 해당 scene으로 간다.
        }

    }

    private void OnCollisionEnter(Collision collision)
    {
        if(collision.gameObject.tag == "Floor")
        {
            isJump = false;
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.tag == "Item")
        {
            itemCount++;
            audio.Play();
            other.gameObject.SetActive(false);
            manager.GetItem(itemCount);
        }
        else if (other.tag == "Finish")
        {
            if(itemCount == manager.totalItemCount)
            {
                //Game clear!
                //SceneManager.LoadScene("Exsample1_" + (manager.stage + 1).ToString());
                SceneManager.LoadScene(manager.stage + 1);
            }
            else
            {
                //Restart..
                //SceneManager.LoadScene("Exsample1_" + manager.stage.ToString());
                SceneManager.LoadScene(manager.stage);
            }
        }
    }
}
