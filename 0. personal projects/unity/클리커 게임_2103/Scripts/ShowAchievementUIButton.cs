using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShowAchievementUIButton : MonoBehaviour
{
    public void ShowUI()
    {
        GooglePlayServiceManager.Instance.ShowAchievementUI();
    }
}
