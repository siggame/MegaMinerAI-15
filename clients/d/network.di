extern (C):

int open_server_connection(const char*, const char*);
int send_string(int, const char*);
char* rec_string(int);
char* escape_string(const char*);
