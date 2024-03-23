//============================================================================
// Name        : queue.cpp
// Author      : Shubham Shinde
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;


template<class T>
class queue
{

	class Node
	{
	public:
		T data;
		Node* next = nullptr;
		Node(int _data) : data(_data){}

		bool operator<=(Node &o)
		{
			return data <= o.data;
		}
	};

public:

	Node* head = nullptr;
	Node* tail = head;


	T front()
	{
		return head->data;
	}

	void pop()
	{
		Node* temp = head;
		if (!temp->next)
		{
			delete temp;
			head = nullptr;
			tail = head;
		}
		else
		{
			temp = head->next;
			head->next = nullptr;
			delete head;
			head = temp;
		}
	}

	bool empty()
	{
		return (head == nullptr);
	}


	void push(T _data)
	{
		if (head == nullptr)
		{
			head = new Node(_data);
			tail = head;
		}
		else
		{
			Node* newNode = new Node(_data);
			Node* temp = head;

			if ((*head <= *newNode))
			{
			    newNode->next = head;
			    head = newNode;
			    return;
			}

			while((temp->next) && (*newNode <= *temp))
				temp = temp->next;
			if (!temp->next)
			{
				tail->next = newNode;
				tail = tail->next;
			}
			else
			{
				newNode->next = temp->next;
				temp->next = newNode;
			}
		}
	}

	void print()
	{
		Node* temp = head;
		while(temp)
		{
			cout<<temp->data<<" ";
			temp = temp->next;
		}
		cout<<endl;
	}
};


int main() {
	queue<char> q;

	while(true)
		{
			int choice = 0;

			cout<<"Here are the Options:-"<<endl;
			cout<<"1. Add jobs: "<<endl;
			cout<<"2. Display Jobs : "<<endl;
			cout<<"3. Delete Jobs"<<endl;
			cout<<endl;

			cin>>choice;

			if (choice == 1)
			{
				char data;
				cout<<"Enter Job Prority"<<endl;
				cin>>data;
				q.push(data);
				q.print();
				cout<<"Job Added Successfully"<<endl;
				cout<<endl;
			}
			else if (choice == 2)
			{
				cout<<"Here are the Jobs "<<endl;
				q.print();
				cout<<endl;
			}
			else if (choice == 3)
			{
				if (!q.empty())
				{
					q.pop();
					cout<<"Job Deleted"<<endl;
					q.print();
					cout<<endl;
				}else
				{
					cout<<"No Job to delete"<<endl;
					cout<<endl;
				}

			}
			else
				break;
		}

	return 0;
}

//Here are the Options:-
//1. Add jobs:
//2. Display Jobs :
//3. Delete Jobs
//
//1
//Enter Job Prority
//5
//5
//Job Added Successfully
//
//Here are the Options:-
//1. Add jobs:
//2. Display Jobs :
//3. Delete Jobs
//
//1
//Enter Job Prority
//10
//10 5
//Job Added Successfully
//
//Here are the Options:-
//1. Add jobs:
//2. Display Jobs :
//3. Delete Jobs
//
//1
//Enter Job Prority
//7
//10 7 5
//Job Added Successfully
//
//Here are the Options:-
//1. Add jobs:
//2. Display Jobs :
//3. Delete Jobs
//
//3
//Job Deleted
//7 5
//
//Here are the Options:-
//1. Add jobs:
//2. Display Jobs :
//3. Delete Jobs
//
//2
//Here are the Jobs
//7 5
//
//Here are the Options:-
//1. Add jobs:
//2. Display Jobs :
//3. Delete Jobs
//
//4

