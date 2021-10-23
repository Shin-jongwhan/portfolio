using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerAction : MonoBehaviour
{
    public float speed;
    public GameManager manager;

    float h;
    float v;
    bool isHorizonMove;
    string TalkObjectName;

    // Mobile key var
    int up_value;
    int down_value;
    int left_value;
    int right_value;
    bool up_down;
    bool down_down;
    bool left_down;
    bool right_down;
    bool up_up;
    bool down_up;
    bool left_up;
    bool right_up;

    Rigidbody2D rigid;
    Animator anim;
    Vector3 dirVec;
    GameObject scanObject;
    
    
    // Start is called before the first frame update
    void Awake()
    {
        rigid = GetComponent<Rigidbody2D>();
        anim = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        // Move value
        // PC & mobile
        h = manager.isAction ? 0 : Input.GetAxisRaw("Horizontal") + right_value + left_value;
        v = manager.isAction ? 0 : Input.GetAxisRaw("Vertical") + up_value + down_value;

        // Check Button Down & Up
        // PC & mobile
        bool hDown = manager.isAction ? false : Input.GetButtonDown("Horizontal") || right_down || left_down;
        bool vDown = manager.isAction ? false : Input.GetButtonDown("Vertical") || up_down || down_down;
        bool hUp = manager.isAction ? false : Input.GetButtonUp("Horizontal") || right_up || left_up;
        bool vUp = manager.isAction ? false : Input.GetButtonUp("Vertical") || up_up || down_up;

        // Check Horizontal Move
        if (hDown || vUp)
            isHorizonMove = true;
        else if (vDown || hUp)
            isHorizonMove = false;
        else if (hUp || vUp)
            isHorizonMove = h != 0;

        // Animation
        if (anim.GetInteger("horizonAxisRaw") != h)     // ���� ���� �ƴ� ���� �־��ش�.
        {
            anim.SetBool("isChange", true);
            anim.SetInteger("horizonAxisRaw", (int)h);
        }
        else if (anim.GetInteger("verticalAxisRaw") != v)
        {
            anim.SetBool("isChange", true);
            anim.SetInteger("verticalAxisRaw", (int)v);
        }
        else
        {
            anim.SetBool("isChange", false);
        }

        // Direction
        if (vDown && v == 1)
            dirVec = Vector3.up;
        else if (vDown && v == -1)
            dirVec = Vector3.down;
        else if (hDown && h == -1)
            dirVec = Vector3.left;
        else if (hDown && h == 1)
            dirVec = Vector3.right;

        // Scan Object
        if (Input.GetButtonDown("Jump") && scanObject != null)
        {
            //Debug.Log("This is : " + scanObject);
            manager.Action(scanObject, TalkObjectName);
        }

        // Mobile var initialization
        up_down = false;
        down_down = false;
        left_down = false;
        right_down = false;
        up_up = false;
        down_up = false;
        left_up = false;
        right_up = false;
    }

    void FixedUpdate()
    {
        Vector2 moveVec = isHorizonMove ? new Vector2(h, 0) : new Vector2(0, v);
        rigid.velocity = moveVec * speed;

        // Ray
        //Debug.Log(rigid.position);
        //Debug.DrawRay�� �̸� ���� RayCast�� �����ϸ� ����!
        Debug.DrawRay(rigid.position, dirVec * 3.5f, new Color(0, 1, 0));       // Ray�� dirVec �������� 0.7f��ŭ ���. Color(0, 1, 0) : ���
        RaycastHit2D rayHit = Physics2D.Raycast(rigid.position, dirVec, 3.5f, LayerMask.GetMask("Object"));     // Layer : "Object"�� �͸� ��ĵ ����
        
        if(rayHit.collider != null)
        {
            scanObject = rayHit.collider.gameObject;        // "Object" layer�� ���� object�� Raycast�� �ν��� ��, �ش� ������Ʈ�� scanObject�� �ν��Ѵ�. 
            TalkObjectName = rayHit.collider.gameObject.name;
        }
        else
        {
            scanObject = null;
        }
    }

    // button���� event trigger ������Ʈ�� �߰�, ��ư�� ������ ���� ������ ���� �����Ͽ� string���� ���� �־��ش�.
    public void ButtonDown(string type)
    {
        switch (type)
        {
            case "U":
                up_value = 1;
                up_down = true;
                break;
            case "D":
                down_value = -1;
                down_down = true;
                break;
            case "L":
                left_value = -1;
                left_down = true;
                break;
            case "R":
                right_value = 1;
                right_down = true;
                break;
            case "A":       // Object scan
                if (scanObject != null)
                {
                    manager.Action(scanObject, TalkObjectName);
                }
                break;
            case "C":       // Cancel
                manager.SubMenuActive();
                break;
        }
    }

    public void ButtonUp(string type)
    {
        switch (type)
        {
            case "U":
                up_value = 0;
                up_up = true;
                break;
            case "D":
                down_value = 0;
                down_up = true;
                break;
            case "L":
                left_value = 0;
                left_up = true;
                break;
            case "R":
                right_value = 0;
                right_up = true;
                break;
        }
    }

}
