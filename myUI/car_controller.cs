using UnityEngine;

public class CarController : MonoBehaviour
{
    public float moveSpeed = 10f;
    public float turnSpeed = 50f;
    
    void Update()
    {
        float vertical = Input.GetAxis("Vertical");
        float horizontal = Input.GetAxis("Horizontal");
        
        // Simple movement
        transform.Translate(0, 0, vertical * moveSpeed * Time.deltaTime);
        transform.Rotate(0, horizontal * turnSpeed * Time.deltaTime, 0);
    }
}
