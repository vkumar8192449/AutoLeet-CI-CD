sourceCode = ["""class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> tmp = nums;
        sort(nums.begin(),nums.end());
        int l=0 , h=nums.size()-1;
        while(true){
            if(nums[l]+nums[h]==target){
                int x=0, y=nums.size()-1;
                while(tmp[x]!=nums[l])x++;
                while(tmp[y]!=nums[h])y--;
                return {x,y};
            }
            else if(nums[l]+nums[h]>target)h--;
            else l++;
        }
        return {};
    }
};""", """/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head==NULL || head->next==NULL){
            return false;
        }
        ListNode* slow=head;
        ListNode* fast=head;
        while(slow->next && fast->next && fast->next->next){
            slow=slow->next;
            fast=fast->next->next;
            if(slow==fast){
                return true;
            }
        }
        return false;
    }
};""",
              """/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* newhead=NULL;
    void func(ListNode* curr, ListNode* prev){
        if(curr->next!=NULL){
            func(curr->next,curr);
        }
        else{
            newhead=curr;
        }
        curr->next=prev;
    }
    ListNode* reverseList(ListNode* head) {
        if(!head)return head;
        func(head,NULL);
        return newhead;
    }                     
};""",
              """/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reverse(ListNode* &tmp, ListNode* curr, ListNode* prev){
        if(curr->next!=NULL){
            reverse(tmp,curr->next,curr);
        }
        else{
            tmp=curr;
        }
        curr->next=prev;
    }
    ListNode* getmiddle(ListNode* head){
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast->next!=NULL && fast->next->next!=NULL){
            slow=slow->next;
            fast=fast->next->next;
        }
        return slow;
    }
    bool isPalindrome(ListNode* head) {
        if(head->next==NULL)return 1;
        ListNode* mid = getmiddle(head);
        ListNode* tmp=NULL;
        reverse(tmp,mid->next,NULL);
        mid->next=tmp;
        mid=mid->next;
        while(mid){
            if(head->val!=mid->val)return 0;
            head=head->next;
            mid=mid->next;
        }
        return 1;
    }
};""",
              """/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* tp=head;
        ListNode* bfrstr=NULL;
        int ind=0;
        while(ind<left-1){
            ind++;
            bfrstr=tp;
            tp=tp->next;
        }
        ListNode* start=tp;
        while(ind<right-1){
            ind++;
            tp=tp->next;
        }
        ListNode* end=tp;
        if(start==end){
            return head;
        }
        tp=NULL;
        while(start!=end){
            tp = start->next;
            start->next=end->next;
            end->next=start;
            start=tp;
        }
        if(bfrstr){
            bfrstr->next=start;
        }
        if(left==1){
            head=start;
        }
        return head;
    }
};""",
              """/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *check(ListNode *head){
        ListNode *slow=head;
        ListNode *fast=head;
        while(true){
            slow=slow->next;
            if(!fast->next)return NULL;
            fast=fast->next->next;
            if(fast==NULL){
                return NULL;
            }
            if(slow==fast){
                return fast;
            }
            
        }
    }
    ListNode *detectCycle(ListNode *head) {
        if(!head || head->next==head)return head;
        if(head->next==NULL)return NULL;
        ListNode* ans= check(head);
        if(ans){
            while(head!=ans){
                head=head->next;
                ans=ans->next;
            }
            return ans; 
        }
        return NULL;
    }
};"""]
