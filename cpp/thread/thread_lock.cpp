#include <iostream>
#include <mutex>
#include <thread>
#include <condition_variable>
std::mutex       g_mutex;   // 用到的全局锁
std::condition_variable g_cond;   // 用到的条件变量

// g++ -std=c++11 thread_lock.cpp -o lock -lpthread

int g_i    = 0;
bool g_running = true;

void ThreadFunc(int n) {       // 线程执行函数
 for (int i = 0; i < n; ++i) {
  {
   std::lock_guard<std::mutex> lock(g_mutex);   // 加锁，离开{}作用域后锁释放
   ++g_i;
   std::cout << "plus g_i by func thread " << std::this_thread::get_id() << std::endl;
  }
 }
 std::unique_lock<std::mutex> lock(g_mutex);    // 加锁
 while (g_running) {
  std::cout << "wait for exit" << std::endl;
  g_cond.wait(lock);                // wait调用后，会先释放锁，之后进入等待状态；当其它进程调用通知激活后，会再次加锁
 }
 std::cout << "func thread exit" << std::endl;
}
int main() {
 int     n = 100;
 std::thread t1(ThreadFunc, n);    // 创建t1线程（func thread），t1会执行`ThreadFunc`中的指令
 for (int i = 0; i < n; ++i) {
  {
   std::lock_guard<std::mutex> lock(g_mutex);
   ++g_i;
   std::cout << "plus g_i by main thread " << std::this_thread::get_id() << std::endl;
  }
 }
 {
  std::lock_guard<std::mutex> lock(g_mutex);
  g_running = false;
  g_cond.notify_one();   // 通知其它线程
 }
 t1.join();     // 等待线程t1结束
 std::cout << "g_i = " << g_i << std::endl;
}
