//============================================================================
// Name        : 8_Linked_List.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

map<string, bool> a;
map<string, bool> b;

class Node
{
public:
    string data;
    Node *next;

    Node() : data(""), next(nullptr) {}
    Node(string _data) : data(_data), next(nullptr) {}
};

void createA(Node *&start, int n)
{
    start = new Node;
    Node* head = start;

    cout << "Enter data " << endl;

    Node *pre = start;

    for (int i = 0; i < n; i++)
    {
        while (true)
        {
            string t = "";
            cin >> t;
            if (!a[t])
            {
                head = new Node(t);
                pre->next = head;
                pre = head;
                a[t] = true;
                break;
            }
            else
                cout << "Data Already Existed" << endl;
        }
    }
}

void createB(Node* &start, int n)
{
    start = new Node;
    Node* head = start;

    cout << "Enter data " << endl;

    Node *pre = head;

    for (int i = 0; i < n; i++)
    {
        while (true)
        {
            string t = "";
            cin >> t;
            if (!b[t])
            {
                head = new Node(t);
                pre->next = head;
                pre = head;
                b[t] = true;
                break;
            }
            else
                cout << "Data Already Existed" << endl;
        }
    }
}

Node *inter(Node *A, Node *B)
{
    Node *temp1, *temp2;
    temp1 = A;
    temp2 = B;

    Node *head = new Node;
    Node *temp3 = head;
    Node *pre = head;

    while (temp1)
    {
        while (temp2)
        {
            if (temp1->data == temp2->data)
            {
                temp3 = new Node;
                temp3->data = temp1->data;
                pre->next = temp3;
                pre = temp3;
            }
            temp2 = temp2->next;
        }
        temp2 = B;
        temp1 = temp1->next;
    }

    return head->next;
}

Node *uni(Node *A, Node *B)
{
    Node *head = new Node;
    Node *temp1 = A;
    Node *temp2 = B;
    Node* temp3 = head;

    Node *pre = head;

    while (temp1)
    {
        temp3 = new Node;
        temp3->data = temp1->data;
        pre->next = temp3;
        pre = temp3;
        temp1 = temp1->next;
    }

    temp1 = A;
    while (temp2)
    {
        bool flag = 0;
        while (temp1)
        {
            if (temp1->data == temp2->data)
                flag = 1;
            temp1 = temp1->next;
        }

        temp1 = A;

        if (!flag)
        {
            temp3 = new Node;
            temp3->data = temp2->data;
            pre->next = temp3;
            pre = temp3;
            flag = 0;
        }
        temp2 = temp2->next;
    }

    return head->next;
}

Node* diff(Node* A , Node* B)
{
	Node *head = new Node;
	Node *temp2 = A;
	Node *temp1 = B;
	Node* temp3 = head;

	Node *pre = head;

	temp1 = B;
	while (temp2)
	{
		bool flag = 0;
		while (temp1)
		{
			if (temp1->data == temp2->data)
				flag = 1;
			temp1 = temp1->next;
		}

		temp1 = B;

		if (!flag)
		{
			temp3 = new Node;
			temp3->data = temp2->data;
			pre->next = temp3;
			pre = temp3;
			flag = 0;
		}
		temp2 = temp2->next;
	}

	return head->next;
}

void display(Node* head)
{
    while(head)
    {
        cout<<head->data<<" ";
        head = head->next;
    }
    cout<<endl;
}

int main()
{
    int n;
    cout << "Enter No of Total Students : ";
    cin >> n;
    cout << endl;

    Node *A = nullptr;
    Node *B = nullptr;

    int a;
    cout << "Enter No of Students Who like Vannilla IceCream : ";
    cin >> a;
    createA(A, a);
    A = A->next;
    cout << endl;

    int b;
    cout << "Enter No of Students Who like butterScoch IceCream : ";
    cin >> b;
    createB(B, b);
    B = B->next;
    cout << endl;

    cout << "Students Who like Vannilla IceCream : ";
    display(A);
    cout << "Students Who like butterScoch IceCream : ";
    display(B);




    while(true)
	{
		int choice = 0;

		cout<<"Here are the Options:-"<<endl;
		cout<<"1. Set Of Student Who Both like vannila and butterscoch : "<<endl;
		cout<<"2. Set of Students who like either Vannila or ButterScoch but not Both : "<<endl;
		cout<<"3. No of Students who dont like Icecream"<<endl;

		cin>>choice;

		if (choice == 1)
		{
			cout<<"Set Of Student Who Both like vannila and butterscoch : "<<endl;
			display(inter(A, B));
		}
		else if (choice == 2)
		{
			cout<<"Set of Students who like either Vannila or ButterScoch but not Both : "<<endl;
			display(diff(uni(A, B), inter(A,B)));
		}
		else if (choice == 3)
		{
			cout<<"No of Students who dont like Icecream : "<<endl;
			int i = 1;
			Node* temp = uni(A,B);
			while(temp)
			{
				temp = temp->next;
				i++;
			}
			cout<<n - i<<endl;

		}
		else
			break;
	}



    return 0;
}

//Enter No of Total Students : 5
//
//Enter No of Students Who like Vannilla IceCream : 3
//Enter data
//2
//5
//6
//
//Enter No of Students Who like butterScoch IceCream : 3
//Enter data
//2
//5
//9
//
//Students Who like Vannilla IceCream : 2 5 6
//Students Who like butterScoch IceCream : 2 5 9
//Here are the Options:-
//1. Set Of Student Who Both like vannila and butterscoch :
//2. Set of Students who like either Vannila or ButterScoch but not Both :
//3. No of Students who dont like Icecream
//1
//Set Of Student Who Both like vannila and butterscoch :
//2 5
//Here are the Options:-
//1. Set Of Student Who Both like vannila and butterscoch :
//2. Set of Students who like either Vannila or ButterScoch but not Both :
//3. No of Students who dont like Icecream
//2
//Set of Students who like either Vannila or ButterScoch but not Both :
//6 9
//Here are the Options:-
//1. Set Of Student Who Both like vannila and butterscoch :
//2. Set of Students who like either Vannila or ButterScoch but not Both :
//3. No of Students who dont like Icecream
//3
//No of Students who dont like Icecream :
//0
//Here are the Options:-
//1. Set Of Student Who Both like vannila and butterscoch :
//2. Set of Students who like either Vannila or ButterScoch but not Both :
//3. No of Students who dont like Icecream
//4

