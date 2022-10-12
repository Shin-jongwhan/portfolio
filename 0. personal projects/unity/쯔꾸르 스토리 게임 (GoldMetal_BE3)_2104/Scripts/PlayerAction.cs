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
        if (anim.GetInteger("horizonAxisRaw") != h)     // 같은 값이 아닐 때만 넣어준다.
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
        //Debug.DrawRay로 미리 보고 RayCast를 구현하면 쉽다!
        Debug.DrawRay(rigid.position, dirVec * 3.5f, new Color(0, 1, 0));       // Ray를 dirVec 방향으로 0.7f만큼 쏜다. Color(0, 1, 0) : 녹색
        RaycastHit2D rayHit = Physics2D.Raycast(rigid.position, dirVec, 3.5f, LayerMask.GetMask("Object"));     // Layer : "Object"인 것만 스캔 가능
        
        if(rayHit.collider != null)
        {
            scanObject = rayHit.collider.gameObject;        // "Object" layer를 가진 object를 Raycast로 인식한 후, 해당 오브젝트를 scanObject에 인식한다. 
            TalkObjectName = rayHit.collider.gameObject.name;
        }
        else
        {
            scanObject = null;
        }
    }

    // button에서 event trigger 컴포넌트를 추가, 버튼이 눌렸을 때와 떼졌을 때를 구분하여 string으로 값을 넣어준다.
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
