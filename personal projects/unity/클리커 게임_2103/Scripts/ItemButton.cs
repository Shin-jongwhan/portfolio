//일정 시간마다(ex) 1초마다) 자동으로 인컴이 들어오게 할 수 있게 하는 script
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ItemButton : MonoBehaviour
{
    //살 수 있으면 upgradableColor, 살 수 없으면 notUpgradableColor
    //public Color upgradableColor = Color.blue;
    //public Color notUpgradableColor = Color.red;
    //public Image colorImage;

    public Text itemDisplayer;

    public CanvasGroup canvasGroup;

    public Slider slider;

    public string itemName;

    public int level; //item은 구매를 해야 레벨 1로 시작

    [HideInInspector]
    public int currentCost;
    public int startCurrentCost = 1;

    [HideInInspector]
    public int goldPerSec;
    public int startGoldPerSec = 1;

    public float costPow = 3.0f;
    public float upgradePow = 2.0f;

    [HideInInspector]
    public bool isPurchased = false;

    private void Start()
    {
        /*
        currentCost = startCurrentCost;
        goldPerSec = startGoldPerSec;
        */
        DataController.Instance.LoadItemButton(this);  //this: 자기 자신. 여기선 ItemButton을 뜻함

        StartCoroutine("AddGoldLoop");  //1초마다 계속 AddGoldLoop가 백그라운드에서 돌아간다

        UpdateUI();
    }

    public void PurchaseItem()
    {
        if(DataController.Instance.gold >= currentCost)
        {
            isPurchased = true;
            DataController.Instance.gold -= currentCost;
            level++;    //level = level + 1;

            UpdateItem();
            UpdateUI();

            DataController.Instance.SaveItemButton(this);
        }
    }

    //co-routine: 일정시간마다 while이 돌아가게 함
    IEnumerator AddGoldLoop()
    {
        while (true)
        {
            if (isPurchased)
            {
                DataController.Instance.gold += goldPerSec;
            }

            yield return new WaitForSeconds(1.0f);  //1초 대기
        }
    }

    public void UpdateItem()
    {
        //아이템 업그레이드할 때마다 인컴 증가량, 가격 증가
        goldPerSec = startGoldPerSec * (int) Mathf.Pow(upgradePow, level);
        currentCost = startCurrentCost * (int)Mathf.Pow(costPow, level);
    }

    public void UpdateUI()
    {
        // isPurchased: true or false
        itemDisplayer.text = itemName + "\nLevel: " + level + "\nCost: " + currentCost + "\nGold Per Sec: " + goldPerSec;

        slider.minValue = 0;
        slider.maxValue = currentCost;
        slider.value = DataController.Instance.gold;    //gold가 maxValue보다 높아도 value 값이 그 이상 커지진 않는다.

        if (isPurchased)
        {
            canvasGroup.alpha = 1.0f;
        }
        else
        {
            canvasGroup.alpha = 0.6f;
        }

        /*
    //살 수 있으면 upgradableColor, 살 수 없으면 notUpgradableColor
    public Color upgradableColor = Color.blue;
    public Color notUpgradableColor = Color.red;
    public Image colorImage;
        이 코드를 쓸 때
        if (currentCost <= DataController.Instance.gold)
        {
            colorImage.color = upgradableColor;
        }
        else
        {
            colorImage.color = notUpgradableColor;
        }
        */
    }

    private void Update()
    {
        UpdateUI();
    }
}
