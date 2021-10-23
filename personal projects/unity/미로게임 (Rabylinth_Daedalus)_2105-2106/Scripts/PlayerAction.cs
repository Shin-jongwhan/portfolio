using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerAction : MonoBehaviour
{
    float h;
    float v;
    bool isFinishLineArrived;

    GameObject scanObject;
    Vector3 dirVec;
    Vector3 currentPos;
    RaycastHit2D rayHitUp;
    RaycastHit2D rayHitDown;
    RaycastHit2D rayHitLeft;
    RaycastHit2D rayHitRight;
    RaycastHit2D rayHitBlockUp;
    RaycastHit2D rayHitBlockDown;
    RaycastHit2D rayHitBlockLeft;
    RaycastHit2D rayHitBlockRight;
    RaycastHit2D rayHitFinish;
    RaycastHit2D rayHitHidePass;
    Rigidbody2D rigid;
    AudioSource walkingSound;
    public Animator anim;
    public GameObject canselPanel;
    public GameObject nextStagePanel;

    // Start is called before the first frame update
    void Start()
    {
        rigid = GetComponent<Rigidbody2D>();
        isFinishLineArrived = false;
        walkingSound = GetComponent<AudioSource>();
    }

    // Update is called once per frame
    void Update()
    {
        // Cancel button�� �������� �� ������� �� �ϰ� ��
        if (canselPanel.activeSelf || nextStagePanel.activeSelf)
            return;

        h = Input.GetAxisRaw("Horizontal");
        v = Input.GetAxisRaw("Vertical");
        anim.SetInteger("hAxisRaw", (int)h);
        anim.SetInteger("vAxisRaw", (int)v);

        //Debug.Log(h);
        //Debug.Log(v);

        if (Input.GetButtonDown("Vertical") && v == 1)
        {
            if (rayHitUp == false)
            {
                walkingSound.Play();
                dirVec = Vector3.up;
                PlayerMoveAction();
            }
            else
            {
                if(rayHitBlockUp == true)
                    rayHitBlockUp.collider.gameObject.SetActive(false);
                Debug.Log("���� ���̴�.");
            }
        }
        else if (Input.GetButtonDown("Vertical") && v == -1)
        {
            if (rayHitDown == false)
            {
                walkingSound.Play();
                dirVec = Vector3.down;
                PlayerMoveAction();
            }
            else
            {
                if(rayHitBlockDown == true)
                    rayHitBlockDown.collider.gameObject.SetActive(false);
                Debug.Log("���� ���̴�.");
            }
        }
        else if (Input.GetButtonDown("Horizontal") && h == -1)
        {
            if (rayHitLeft == false)
            {
                walkingSound.Play();
                dirVec = Vector3.left;
                PlayerMoveAction();
            }
            else
            {
                if(rayHitBlockLeft == true)
                    rayHitBlockLeft.collider.gameObject.SetActive(false);
                Debug.Log("���� ���̴�.");
            }
        }
        else if (Input.GetButtonDown("Horizontal") && h == 1)
        {
            if (rayHitRight == false)
            {
                walkingSound.Play();
                dirVec = Vector3.right;
                PlayerMoveAction();
            }
            else
            {
                if(rayHitBlockRight == true)
                    rayHitBlockRight.collider.gameObject.SetActive(false);
                Debug.Log("���� ���̴�.");
            }
        }

    }

    void FixedUpdate()
    {
        // ��ü ����
        //Debug.DrawRay(rigid.position, dirVec * 3.5f, new Color(0, 1, 0));       // Ray�� dirVec �������� 0.7f��ŭ ���. Color(0, 1, 0) : ���
        //RaycastHit2D rayHit = Physics2D.Raycast(rigid.position, dirVec, 3.5f, LayerMask.GetMask("Object"));     // Layer : "Object"�� �͸� ��ĵ ����
        Debug.DrawRay(rigid.position, Vector3.up * 1.2f, new Color(0, 1, 0));       // ��
        Debug.DrawRay(rigid.position, Vector3.down * 1.2f, new Color(0, 1, 0));     // �Ʒ�
        Debug.DrawRay(rigid.position, Vector3.left * 1.2f, new Color(0, 1, 0));     // ����
        Debug.DrawRay(rigid.position, Vector3.right * 1.2f, new Color(0, 1, 0));        // ������
        
        rayHitUp = Physics2D.Raycast(rigid.position, Vector3.up, 1.2f, LayerMask.GetMask("Object"));
        rayHitDown = Physics2D.Raycast(rigid.position, Vector3.down, 1.2f, LayerMask.GetMask("Object"));
        rayHitLeft = Physics2D.Raycast(rigid.position, Vector3.left, 1.2f, LayerMask.GetMask("Object"));
        rayHitRight = Physics2D.Raycast(rigid.position, Vector3.right, 1.2f, LayerMask.GetMask("Object"));
        rayHitBlockUp = Physics2D.Raycast(rigid.position, Vector3.up, 1.2f, LayerMask.GetMask("Hide space"));
        rayHitBlockDown = Physics2D.Raycast(rigid.position, Vector3.down, 1.2f, LayerMask.GetMask("Hide space"));
        rayHitBlockLeft = Physics2D.Raycast(rigid.position, Vector3.left, 1.2f, LayerMask.GetMask("Hide space"));
        rayHitBlockRight = Physics2D.Raycast(rigid.position, Vector3.right, 1.2f, LayerMask.GetMask("Hide space"));
        rayHitFinish = Physics2D.Raycast(rigid.position, Vector3.down, 0.2f, LayerMask.GetMask("Finish line"));
        rayHitHidePass = Physics2D.Raycast(rigid.position, Vector3.down, 0.2f, LayerMask.GetMask("Hide space"));

        if (rayHitFinish.collider != null && isFinishLineArrived == false)
        {
            nextStagePanel.SetActive(true);
            Debug.Log("�ǴϽ� ���ο� �����Ͽ����ϴ�. ���ϵ帳�ϴ�!");
            isFinishLineArrived = true;
        }
        else if (rayHitFinish.collider == null)
            isFinishLineArrived = false;

        //Debug.Log(rayHitHidePass.collider);
        if (rayHitHidePass.collider != null)
        {
            Debug.Log(rayHitHidePass.collider);
            scanObject = rayHitHidePass.collider.gameObject;
            scanObject.SetActive(false);
        }

    }

    void PlayerMoveAction()
    {
        currentPos = this.gameObject.transform.position;
        transform.position = new Vector3(currentPos.x + dirVec.x, currentPos.y + dirVec.y, dirVec.z);
    }

}
