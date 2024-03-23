//============================================================================
// Name        : 9_stack.cpp
// Author      : Shubham Shinde
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
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

int main() {
	while(true)
	{
		cout<<"Welcome To Valid Parenthesis Checker : "<<endl;
		cout<<"Enter Expression : ";
		string str1;
		cin>>str1;
		if (valid(str1))
				cout<<"It is Valid Expression"<<endl;
		else
			cout<<"Not a Valid Expression"<<endl;

		break;
	}
	return 0;
}

//Welcome To Valid Parenthesis Checker :
//Enter Expression : ((a+b)*(c-d])
//Not a Valid Expression
