#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
	bool data;
	Node* next;
	Node* pre;

	Node(): data(0), next(this), pre(this){}
	Node(bool _data): data(_data), next(this), pre(this){}
};



	void display(Node* head)
	{
		int i = 0;
		while(i < 7)
		{
			cout<<head->data<<" ";
			head = head->next;
			i++;
		}
		cout<<endl;
	}

	bool check(Node* head, int n)
	{
		int temp = 0;
		int track = 0;
		Node* start = head;
		while(true)
		{
			if (start == head)
				track++;
			if (track == 3)
				break;

			if (start->data == 0)
				temp++;
			else
				temp = 0;

			if (temp == n)
			{
				while(temp > 0)
				{
					start->data = 1;
					start = start->pre;
					temp--;
				}
				return true;
			}
			start = start->next;
		}
		return false;
	}


	void create(Node* head)
	{
		Node *pre = head->pre;

		int i = 0;
		while (i < 6)
		{
			Node *pre = head->pre;

			Node* newNode = new Node;

			head->pre = newNode;
			newNode->next = head;

			pre->next = newNode;
			newNode->pre = pre;

			i++;
		}

	}

	void del1(Node* head , int j)
	{
		Node* start = head;
		while(j > 0)
		{
			start = start->next;
			j--;
		}
		if (start->data)
		{
			start->data = false;
			cout<<"Tickets Cancelled !"<<endl;
		}
		else
		{
			cout<<"Seat is Not Booked !"<<endl;
		}
	}





int main() {
	Node* rowHead = new Node[10];

	int i = 0;
	while(i < 10)
		create((&rowHead[i++]));

	(rowHead + 1)-> next->next->next->data = 1;
	(rowHead + 2)-> next->next->data = 1;
	(rowHead + 3)-> next->next->data = 1;

	(rowHead + 4)-> next->next->next->data = 1;
	(rowHead + 1)-> next->next->data = 1;
	(rowHead + 5)-> next->next->next->data = 1;
	(rowHead + 6)-> next->next->data = 1;
	(rowHead + 7)-> next->next->next->data = 1;
	(rowHead + 8)-> next->next->data = 1;
	check(&rowHead[5], 3);

	while(true)
	{
		int choice = 0;

		cout<<"Here are the Options:-"<<endl;
		cout<<"1. List of Available Seats : "<<endl;
		cout<<"2. Book Seats : "<<endl;
		cout<<"3. Cancel Booking"<<endl;

		cin>>choice;

		if (choice == 1)
		{
			i = 0;
			while(i < 10)
				display(&rowHead[i++]);
		}
		else if (choice == 2)
		{
			i = 0;
			while(i < 10)
				display(&rowHead[i++]);

			int n ;
			cout<<"How many Tickets do you want to book ? : ";
			cin>>n;

			cout<<"In Which Row do you want seats? : ";
			cin>>i;

			if (check(&rowHead[i], n))
				cout<<"Congrats! Tickets are Booked..."<<endl;
			else
				cout<<"No Available Seats in "<<i<<" row"<<endl;
		}
		else if (choice == 3)
		{

			i = 0;
			while(i < 10)
				display(&rowHead[i++]);

			int i = 0;
			int j = 0;
			cout<<"Enter The Row Number ? : ";
			cin>>i;
			cout<<"Enter The Column Number ? : ";
			cin>>j;

			if (!(i < 10 && j < 7))
				cout<<"No such Seat present."<<endl;
			else
				del1(&rowHead[i], j);
		}
		else
			break;
	}
	return 0;
}

//Here are the Options:-
//1. List of Available Seats :
//2. Book Seats :
//3. Cancel Booking
//1
//0 0 0 0 0 0 0
//0 0 1 1 0 0 0
//0 0 1 0 0 0 0
//0 0 1 0 0 0 0
//0 0 0 1 0 0 0
//1 1 1 1 0 0 0
//0 0 1 0 0 0 0
//0 0 0 1 0 0 0
//0 0 1 0 0 0 0
//0 0 0 0 0 0 0
//Here are the Options:-
//1. List of Available Seats :
//2. Book Seats :
//3. Cancel Booking
//2
//0 0 0 0 0 0 0
//0 0 1 1 0 0 0
//0 0 1 0 0 0 0
//0 0 1 0 0 0 0
//0 0 0 1 0 0 0
//1 1 1 1 0 0 0
//0 0 1 0 0 0 0
//0 0 0 1 0 0 0
//0 0 1 0 0 0 0
//0 0 0 0 0 0 0
//How many Tickets do you want to book ? : 4
//In Which Row do you want seats? : 1
//Congrats! Tickets are Booked...
//Here are the Options:-
//1. List of Available Seats :
//2. Book Seats :
//3. Cancel Booking
//1
//0 0 0 0 0 0 0
//1 0 1 1 1 1 1
//0 0 1 0 0 0 0
//0 0 1 0 0 0 0
//0 0 0 1 0 0 0
//1 1 1 1 0 0 0
//0 0 1 0 0 0 0
//0 0 0 1 0 0 0
//0 0 1 0 0 0 0
//0 0 0 0 0 0 0
//Here are the Options:-
//1. List of Available Seats :
//2. Book Seats :
//3. Cancel Booking
//3
//0 0 0 0 0 0 0
//1 0 1 1 1 1 1
//0 0 1 0 0 0 0
//0 0 1 0 0 0 0
//0 0 0 1 0 0 0
//1 1 1 1 0 0 0
//0 0 1 0 0 0 0
//0 0 0 1 0 0 0
//0 0 1 0 0 0 0
//0 0 0 0 0 0 0
//Enter The Row Number ? : 1
//Enter The Column Number ? : 4
//Tickets Cancelled !
//Here are the Options:-
//1. List of Available Seats :
//2. Book Seats :
//3. Cancel Booking
//1
//0 0 0 0 0 0 0
//1 0 1 1 0 1 1
//0 0 1 0 0 0 0
//0 0 1 0 0 0 0
//0 0 0 1 0 0 0
//1 1 1 1 0 0 0
//0 0 1 0 0 0 0
//0 0 0 1 0 0 0
//0 0 1 0 0 0 0
//0 0 0 0 0 0 0
//Here are the Options:-
//1. List of Available Seats :
//2. Book Seats :
//3. Cancel Booking
//4

