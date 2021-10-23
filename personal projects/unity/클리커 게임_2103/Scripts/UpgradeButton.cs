using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UpgradeButton : MonoBehaviour
{
    //업그레이드할 때 화면에다 띄어줄 수 있도록하는 Text
    public Text UpgradeDisplayer;

    public string upgradeName;

    [HideInInspector]   //public이지만 inspector 상에서는 수정할 수 없도록 함
    //goldByUpgrade를 통해 계속 업글시 goldPerClick 증가량이 증가하게 함
    public int goldByUpgrade;
    //맨 처음 업그레이드 했을 때는 baseGoldByUpgrade
    public int startGoldByUpgrade = 1;

    [HideInInspector]
    public int currentCost = 1; //현재 아이템 업그레이드 가격
    public int startCurrentCost = 1;

    [HideInInspector]
    public int level = 1;

    //업그레이드하면 goldPerClick을 얼마나(몇배로) 증가시킬 것이냐
    public float upgradePow = 1.07f;   

    //업그레이드하면 다음 업그레이드할 때 얼마나 비싸게 할 것이냐
    public float costPow = 3.14f;

    void Start()    //Awake()가 좀 더 빠르다.
    {
        /*
        currentCost = startCurrentCost;
        level = 1;
        goldByUpgrade = startGoldByUpgrade;
        */
        //데이터를 가져옴
        DataController.Instance.LoadUpgradeButton(this);   //this: 자기 자신을 짚어넣는 것
        UpdateUI();
    }

    public void PurchaseUpgrade()
    {
        //static을 이용해서 클래스 이름(DataController)에 
        //.을 찍어서 바로 접근 가능
        if( DataController.Instance.gold >= currentCost)
        {
            //지금 가격보다 gold가 많거나 같으면 아이템 살 수 있게 함
            DataController.Instance.gold -= currentCost;
            level++;
            DataController.Instance.goldPerClick += goldByUpgrade;

            UpdateUpgrade();
            UpdateUI();
            DataController.Instance.SaveUpgradeButton(this);   //this: 자기 자신을 짚어넣는 것
        }
    }

    public void UpdateUpgrade()
    {
        //pow: 제곱을 나타냄 ex) 2의 '2승, 3승'
        //Mathf.Pow(upgradePow, level): upgradePoew의 level만큼 제곱한 수
        //Mathf.Pow는 float이기 때문에 int형으로 명시적으로 변환
        goldByUpgrade = startGoldByUpgrade * (int) Mathf.Pow(upgradePow, level);
        currentCost = startCurrentCost * (int)Mathf.Pow(costPow, level);
    }

    public void UpdateUI()
    {
        UpgradeDisplayer.text = upgradeName + "\nCost: " + currentCost + "\nLevel: " + level + "\nNext New GoldPerClick: " + goldByUpgrade;
    }

}
