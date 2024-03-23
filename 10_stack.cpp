//============================================================================
// Name        : 10_stack.cpp
// Author      : Shubham Shinde
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

template<class T>
class stack
{
	int size;
	T *arr;
	int t;

public:
	stack(int _size) : size(_size), t(-1) {arr = new T(size);};

	void pop()
	{
		t--;
	}

	void push(T _data)
	{
		arr[++t] = _data;
	}

	T top()
	{
		return arr[t];
	}

	bool empty()
	{
		return t == -1;
	}
};

bool valid(string s)
{
	stack<char> st(30);

	for (auto ch : s)
	{
		if (ch == '(' || ch == '{' || ch == '[')
			st.push(ch);
		else if (ch == ')' || ch =='}' || ch == ']')
		{
			if (st.empty())
				return false;

			else if ((ch == ')' && st.top() == '(') || (ch == '}' && st.top() == '{') || (ch == ']' && st.top() == '['))
				st.pop();
			else
				return false;
		}
	}

	return st.empty();

}

string postfix(string s)
{
	stack<char> st1(30);
	stack<char> st2(30);

	string ans = "";

	for (auto ch : s)
	{
		if (ch == '(' || ch == '{' ||ch == '[')
			continue;

		else if (ch == ')' || ch == '}' || ch == ']')
		{
			string temp = "";
			for (int i = 0; i < 2 ; i++)
			{
				if (!st1.empty())
				{
					temp = st1.top() + temp;
					st1.pop();
				}
			}
			ans = ans + temp;
			ans += st2.top();
			st2.pop();
		}

		else if (ch == '+' || ch == '-' || ch == '*' || ch == '/')
			st2.push(ch);

		else
			st1.push(ch);
	}

	return ans;
}

int main() {
	cout<<"Welcome To PostFix Converter : "<<endl;
	cout<<"Enter Expression : ";
	string str1;
	cin>>str1;
	if (!valid(str1))
	{
		cout<<"expression is not valid";
		return 0;
	}
	cout<<"PostFix is ; ";
	cout<<postfix(str1)<<endl;

	return 0;
}

//
//Welcome To PostFix Converter :
//Enter Expression : ((a+b)*(c-d))
//PostFix is ; ab+cd-*
