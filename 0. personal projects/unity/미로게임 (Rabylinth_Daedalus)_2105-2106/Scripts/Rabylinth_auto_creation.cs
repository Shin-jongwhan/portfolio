using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rabylinth_auto_creation : MonoBehaviour
{
    int nMaze_x;
    int nMaze_y;
    int[] lsMaze_start_line;
    int[] lsMaze_finish_line;
    int[,] lsMaze;

    private void Start()
    {
        nMaze_x = Random.Range(15, 20);
        nMaze_y = Random.Range(15, 20);
        //lsMaze = new int[nMaze_x, nMaze_y];
        Debug.Log("Maze_size : " + nMaze_x + ", " + nMaze_y);

        recursive_backtracking(nMaze_x, nMaze_y);

        //lsMaze_start_line = new int[2] { Random.Range(0, nMaze_x), Random.Range(0, nMaze_y) };
        //Debug.Log("Start_line : " + lsMaze_start_line[0] + ", " + lsMaze_start_line[1]);

        // shuffle 테스트
        //int[,] lsNext_track_tmp = new int[4, 2];
        //lsNext_track_tmp = new int[4,2] { { 1, 2 }, { 3, 4 }, { 5, 6 }, { 7, 8 } };
        //Debug.LogFormat("lsNext_track_tmp in start : {0} {1}, {2} {3}, {4} {5}, {6} {7}", lsNext_track_tmp[0, 0], lsNext_track_tmp[0, 1], lsNext_track_tmp[1, 0], lsNext_track_tmp[1, 1], lsNext_track_tmp[2, 0], lsNext_track_tmp[2, 1], lsNext_track_tmp[3, 0], lsNext_track_tmp[3, 1]);
        //lsNext_track_tmp = ShuffleArray_two_dimension(lsNext_track_tmp);
        //Debug.LogFormat("lsNext_track_tmp in start next shuffle : {0} {1}, {2} {3}, {4} {5}, {6} {7}", lsNext_track_tmp[0, 0], lsNext_track_tmp[0, 1], lsNext_track_tmp[1, 0], lsNext_track_tmp[1, 1], lsNext_track_tmp[2, 0], lsNext_track_tmp[2, 1], lsNext_track_tmp[3, 0], lsNext_track_tmp[3, 1]);
    }

    void recursive_backtracking(int nMaze_x, int nMaze_y)
    {
        lsMaze = new int[nMaze_x, nMaze_y];
        lsMaze_start_line = new int[2] { Random.Range(0, nMaze_x), Random.Range(0, nMaze_y) };
        Debug.Log("Start_line : " + lsMaze_start_line[0] + ", " + lsMaze_start_line[1]);

        for (int i = 0; i < nMaze_x; i++)
        {
            for (int j = 0; j < nMaze_y; j++)
            {
                lsMaze[i, j] = 0;       // initialization. 나중에 1은 갈 수 있는 곳, 0은 막힌 길로 설정
                //Debug.LogFormat("lsMaze[{0}, {1}] : {2}", i, j, lsMaze[i, j]);
            }
        }

        /*  테스트
        lsMaze[0, 0] = 1;
        lsMaze[0, 1] = 2;
        Debug.Log("lsMaze[0, 0] : " + lsMaze[0, 0]);
        Debug.Log("lsMaze[0, 1] : " + lsMaze[0, 1]);
        */

        bool blComback_start_line = false;
        int[] lsPast_track = new int[] { -1, -1 };         // initialization
        int?[,] lsTracking_follow_up = new int?[9999,2];      // initialization. x, y 좌표. ? : 초기 값을 null로 설정해줌
        lsMaze[lsMaze_start_line[0], lsMaze_start_line[1]] = 1;
        //if (lsTracking_follow_up[0, 0] == nul`l)
        //    Debug.Log("lsTracking_follow_up[0, 0] : " + lsTracking_follow_up[0, 0]);

        int nTracking_x = 0;
        int nTest = 0;
        while (blComback_start_line == false)
        {
            Debug.Log("1 Start_line : " + lsMaze_start_line[0] + ", " + lsMaze_start_line[1]);
            int[,] lsNext_track_tmp = new int[4, 2];        // x, y 좌표
            // up, down, left, right
            if (lsTracking_follow_up[0, 0] == null)
            {
                lsNext_track_tmp = new int[4, 2] { { lsMaze_start_line[0] - 1, lsMaze_start_line[1] }, 
                                                   { lsMaze_start_line[0] + 1, lsMaze_start_line[1] }, 
                                                   { lsMaze_start_line[0], lsMaze_start_line[1] - 1 }, 
                                                   { lsMaze_start_line[0], lsMaze_start_line[1] + 1 } };
                lsTracking_follow_up[nTracking_x, 0] = lsMaze_start_line[0];
                lsTracking_follow_up[nTracking_x, 1] = lsMaze_start_line[1];
                lsPast_track[0] = lsMaze_start_line[0];
                lsPast_track[1] = lsMaze_start_line[1];
                Debug.LogFormat("p1 lsNext_track_tmp : {0} {1}, {2} {3}, {4} {5}, {6} {7}", lsNext_track_tmp[0, 0], lsNext_track_tmp[0, 1], lsNext_track_tmp[1, 0], lsNext_track_tmp[1, 1], lsNext_track_tmp[2, 0], lsNext_track_tmp[2, 1], lsNext_track_tmp[3, 0], lsNext_track_tmp[3, 1]);
                Debug.LogFormat("p1 lsTracking_follow_up : {0} {1}", lsTracking_follow_up[nTracking_x, 0], lsTracking_follow_up[nTracking_x, 1]);
            }
            else
            {
                // 다음 갈 수 있는 상하좌우 x, y 좌표 배열.
                lsNext_track_tmp = new int[4, 2] { { (int) lsTracking_follow_up[nTracking_x, 0] - 1, (int) lsTracking_follow_up[nTracking_x, 1] },
                                                   { (int) lsTracking_follow_up[nTracking_x, 0] + 1, (int) lsTracking_follow_up[nTracking_x, 1] },
                                                   { (int) lsTracking_follow_up[nTracking_x, 0], (int) lsTracking_follow_up[nTracking_x, 1] - 1 },
                                                   { (int) lsTracking_follow_up[nTracking_x, 0], (int) lsTracking_follow_up[nTracking_x, 1] + 1 } };
                Debug.LogFormat("p2 lsNext_track_tmp : {0} {1}, {2} {3}, {4} {5}, {6} {7}", lsNext_track_tmp[0, 0], lsNext_track_tmp[0, 1], lsNext_track_tmp[1, 0], lsNext_track_tmp[1, 1], lsNext_track_tmp[2, 0], lsNext_track_tmp[2, 1], lsNext_track_tmp[3, 0], lsNext_track_tmp[3, 1]);
            }
            //Debug.Log("nTest : " + nTest);
            Debug.Log("2 Start_line : " + lsMaze_start_line[0] + ", " + lsMaze_start_line[1]);

            lsNext_track_tmp = ShuffleArray_two_dimension(lsNext_track_tmp);
            Debug.LogFormat("p2 lsNext_track_tmp after shuffle : {0} {1}, {2} {3}, {4} {5}, {6} {7}", lsNext_track_tmp[0, 0], lsNext_track_tmp[0, 1], lsNext_track_tmp[1, 0], lsNext_track_tmp[1, 1], lsNext_track_tmp[2, 0], lsNext_track_tmp[2, 1], lsNext_track_tmp[3, 0], lsNext_track_tmp[3, 1]);
            bool blBreak_i_idx = true;
            for (int i = 0; i < lsNext_track_tmp.GetLength(0); i++)
            {
                if (lsNext_track_tmp[i, 0] < 0
                    || lsNext_track_tmp[i, 1] < 0
                    || lsNext_track_tmp[i, 0] > (nMaze_x - 1)
                    || lsNext_track_tmp[i, 1] > (nMaze_y - 1))
                {
                    continue;
                }
                Debug.LogFormat("p3 lsNext_track_tmp : {0} {1}", lsNext_track_tmp[i, 0], lsNext_track_tmp[i, 1]);
                // 갔었던 길이면 continue
                if (lsMaze[lsNext_track_tmp[i, 0], lsNext_track_tmp[i, 1]] == 0)
                {
                    Debug.LogFormat("p3-2 lsNext_track_tmp : {0} {1}", lsNext_track_tmp[i, 0], lsNext_track_tmp[i, 1]);
                    /////////////////////////////////////////////////////////////////////////////////////
                    // 다음 갈 길에서 인접한 곳에 갔었던 곳이 있는지 체크, 있다면 가지 못 하게 함
                    // 다음 갈 수 있는 길의 상하좌우 x, y 좌표 배열.
                    int[,] lsNext_2_track_tmp = new int[4, 2];
                    lsNext_2_track_tmp = new int[4, 2] { { lsNext_track_tmp[i, 0] - 1, lsNext_track_tmp[i, 1] },
                                                        { lsNext_track_tmp[i, 0] + 1, lsNext_track_tmp[i, 1] },
                                                        { lsNext_track_tmp[i, 0], lsNext_track_tmp[i, 1] - 1 },
                                                        { lsNext_track_tmp[i, 0], lsNext_track_tmp[i, 1] + 1 } };
                    //Debug.LogFormat("p3-3 lsNext_2_track_tmp : {0} {1}, {2} {3}, {4} {5}, {6} {7}", lsNext_2_track_tmp[0, 0], lsNext_2_track_tmp[0, 1], lsNext_2_track_tmp[1, 0], lsNext_2_track_tmp[1, 1], lsNext_2_track_tmp[2, 0], lsNext_2_track_tmp[2, 1], lsNext_2_track_tmp[3, 0], lsNext_2_track_tmp[3, 1]);
                    bool blTrack_check = true;
                    for (int j = 0; j < lsNext_2_track_tmp.GetLength(0); j++)
                    {
                        if (lsNext_2_track_tmp[j, 0] < 0
                        || lsNext_2_track_tmp[j, 1] < 0
                        || lsNext_2_track_tmp[j, 0] > (nMaze_x - 1)
                        || lsNext_2_track_tmp[j, 1] > (nMaze_y - 1))
                        {
                            continue;
                        }
                        //Debug.LogFormat("p3-3 lsNext_2_track_tmp : {0} {1}, {2} {3}, {4} {5}, {6} {7}", lsNext_2_track_tmp[0, 0], lsNext_2_track_tmp[0, 1], lsNext_2_track_tmp[1, 0], lsNext_2_track_tmp[1, 1], lsNext_2_track_tmp[2, 0], lsNext_2_track_tmp[2, 1], lsNext_2_track_tmp[3, 0], lsNext_2_track_tmp[3, 1]);

                        // 온 길이면 continue
                        Debug.LogFormat("p3-3-1 lsNext_2_track_tmp j, lsNext_track_tmp i : {0}, {1} / {2}, {3} ", lsNext_2_track_tmp[j, 0], lsNext_2_track_tmp[j, 1], lsNext_track_tmp[i, 0], lsNext_track_tmp[i, 1]);
                        Debug.LogFormat("p3-3-1 lsPast_track : {0} {1}, lsNext_2_track_tmp : {2} {3}", lsPast_track[0], lsPast_track[1], lsNext_2_track_tmp[j, 0], lsNext_2_track_tmp[j, 1]);
                        if (lsNext_2_track_tmp[j, 0] == lsPast_track[0]
                                && lsNext_2_track_tmp[j, 1] == lsPast_track[1])
                        {
                            continue;
                        }
                        Debug.LogFormat("p3-3 lsNext_2_track_tmp : {0} {1}, {2} {3}, {4} {5}, {6} {7}", lsNext_2_track_tmp[0, 0], lsNext_2_track_tmp[0, 1], lsNext_2_track_tmp[1, 0], lsNext_2_track_tmp[1, 1], lsNext_2_track_tmp[2, 0], lsNext_2_track_tmp[2, 1], lsNext_2_track_tmp[3, 0], lsNext_2_track_tmp[3, 1]);
                        Debug.LogFormat("p3-3 lsMaze[{0}, {1}] : {2}", lsNext_2_track_tmp[j, 0], lsNext_2_track_tmp[j, 1], lsMaze[lsNext_2_track_tmp[j, 0], lsNext_2_track_tmp[j, 1]]);
                        if (lsMaze[lsNext_2_track_tmp[j, 0], lsNext_2_track_tmp[j, 1]] == 1)
                            blTrack_check = false;
                    }
                    if (blTrack_check == false)
                        continue;
                    Debug.Log("3-1 Start_line : " + lsMaze_start_line[0] + ", " + lsMaze_start_line[1]);
                    /////////////////////////////////////////////////////////////////////////////////////
                    // 길 만들어질 경우 결과 입력
                    lsMaze[lsNext_track_tmp[i, 0], lsNext_track_tmp[i, 1]] = 1;
                    nTracking_x++;
                    lsTracking_follow_up[nTracking_x, 0] = lsNext_track_tmp[i, 0];
                    lsTracking_follow_up[nTracking_x, 1] = lsNext_track_tmp[i, 1];
                    lsPast_track[0] = lsNext_track_tmp[i, 0];
                    Debug.Log("3-1-1 Start_line : " + lsMaze_start_line[0] + ", " + lsMaze_start_line[1]);
                    lsPast_track[1] = lsNext_track_tmp[i, 1];
                    Debug.Log("3-1-2 Start_line : " + lsMaze_start_line[0] + ", " + lsMaze_start_line[1]);
                    Debug.LogFormat("p4 lsMaze[{0}, {1}] : {2} ", lsNext_track_tmp[i, 0], lsNext_track_tmp[i, 1], lsMaze[lsNext_track_tmp[i, 0], lsNext_track_tmp[i, 1]]);
                    Debug.LogFormat("p4-1 {0} lsTracking_follow_up : {1} {2}", nTracking_x, lsTracking_follow_up[nTracking_x, 0], lsTracking_follow_up[nTracking_x, 1]);
                    Debug.Log("3-2 Start_line : " + lsMaze_start_line[0] + ", " + lsMaze_start_line[1]);

                    break;
                }

                if (i == (lsNext_track_tmp.GetLength(0) - 1) 
                    && lsTracking_follow_up[nTracking_x, 0] == lsPast_track[0] 
                    && lsTracking_follow_up[nTracking_x, 1] == lsPast_track[1])
                {
                    
                    nTracking_x--;
                    Debug.Log("4 Start_line : " + lsMaze_start_line[0] + ", " + lsMaze_start_line[1]);
                    Debug.LogFormat("p4-2-1 {0} lsTracking_follow_up : {1} {2}", nTracking_x, lsTracking_follow_up[nTracking_x, 0], lsTracking_follow_up[nTracking_x, 1]);
                    lsPast_track[0] = (int) lsTracking_follow_up[nTracking_x, 0];
                    lsPast_track[1] = (int) lsTracking_follow_up[nTracking_x, 1];
                    if (lsTracking_follow_up[nTracking_x, 0] == lsMaze_start_line[0] && lsTracking_follow_up[nTracking_x, 1] == lsMaze_start_line[1])
                    {
                        blComback_start_line = true;
                        Debug.Log("p6 !!!!!!!!!!!recursive backtracking end !!!!!!!!!!!!!!!!");
                        Debug.LogFormat("p6 {0}, lsTracking_follow_up {1} {2}, lsMaze_start_line {3} {4}", nTracking_x, lsTracking_follow_up[nTracking_x, 0], lsTracking_follow_up[nTracking_x, 1], lsMaze_start_line[0], lsMaze_start_line[1]); ;
                    }
                }

                if (i == lsNext_track_tmp.GetLength(0) - 1)
                {
                    blBreak_i_idx = false;
                }
                Debug.Log("p5 check");
            }
            //if (blBreak_i_idx == false)
            //    nTracking_x++;
            nTest++;
            if (nTest == 10000)
            {
                Debug.Log("Recursive_backtracking failed");
                blComback_start_line = true;
            }
        } //while end

        string maze_x_tmp = "";
        for (int i = 0; i < lsMaze.GetLength(0); i++)
        {
            for (int j = 0; j < lsMaze.GetLength(1); j++)
            {
                if (j == 0)
                    maze_x_tmp += i.ToString() + ": ";
                if (j != lsMaze.GetLength(1) - 1)
                    maze_x_tmp += " " + lsMaze[i, j].ToString();
                else
                {
                    maze_x_tmp += " " + lsMaze[i, j].ToString() + "\r\n";
                    //Debug.Log("index : " + i + ", " + maze_x_tmp);
                    Debug.Log(maze_x_tmp);
                    //maze_x_tmp = "";
                }
            }
            
        }
    }

    public static T[,] ShuffleArray_two_dimension<T>(T[,] array)
    {
        int random1;
        int random2;

        T tmp1;
        T tmp2;

        for (int i = 0; i < array.GetLength(0); i++)
        {
            random1 = Random.Range(0, array.GetLength(0));
            random2 = Random.Range(0, array.GetLength(0));

            tmp1 = array[random1, 0];
            tmp2 = array[random1, 1];
            array[random1, 0] = array[random2, 0];
            array[random1, 1] = array[random2, 1];
            array[random2, 0] = tmp1;
            array[random2, 1] = tmp2;
        }

        /*
        for (int i = 0; i < array.GetLength(0); i++)
        {
            Debug.LogFormat("{0} ShuffleArray_two_dimension : {1} {2}", i, array[i, 0], array[i, 1]);
        }
        */

        return array;
    }


}
