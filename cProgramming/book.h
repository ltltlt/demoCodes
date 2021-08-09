#ifndef BOOK_INCLUDED
#define BOOK_INCLUDED
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stddef.h>
#include<assert.h>
#include<time.h>
#include<ctype.h>
#define hashNumber 47
#include"list.h"
typedef struct dirc{
	char* name;
	listptr allbook;
	struct dirc* next;
	int number;
}dirc,*dircptr;
typedef struct book{
	char* name;
	time_t t;
	char* author;
	char* comment;
}book;
extern dircptr hashtable[hashNumber];
extern int add(dircptr ,char* book,char* author,char* comment,time_t );
extern int del(dircptr ,char* );
extern int addDir(char* );
extern int delDir(char* );
extern void show(FILE* ,int );
extern void showDir(void);
extern void showList(void);
extern int showOne(char*);
extern void toFile(void);
extern int addBook(char* dir,char* book,char* author,char* comment,time_t );
extern int delBook(char* ,char* );
extern int delInRead(char* );
extern void list(FILE* ,dircptr );
extern void readFile(void);
extern void showRead(FILE*);
extern size_t hash(const char*);
extern int changeAuthor(char* ,char* ,char* );
extern int changeComment(char* , char* ,char* );
extern dircptr searchDir(const char* );
extern void toLittle(char* ,const char* );
#endif
