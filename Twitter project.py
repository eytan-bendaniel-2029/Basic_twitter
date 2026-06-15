users = {}
posts = []
post_id = 66

def create_user(username, email):
    if username in users:
        print(f"Error: Username '{username}' already exists!")
    else:
        users[username] = {
            "username": username,
            "email": email,
            "followers": [],
            "following": [],
            "liked_posts": []
        }
        print(f"User '{username}' created successfully!")

def create_post(username, content):
    global post_id
    if username not in users:
        print(f"Error: User '{username}' does not exist!")
    else:
        new_post = {
            "id": post_id,
            "author": username,
            "content": content,
            "timestamp": "2026-05-04 11:03:32",
            "likes": 0
        }
        posts.append(new_post)
        post_id += 1
        print(f"Post created successfully! Post ID: {new_post['id']}")

def view_feed(username):
    if username not in users:
        print(f"Error: User '{username}' does not exist!")
    else:
        following_list = users[username]["following"]
        if not following_list:
            print(f"You are not following anyone yet!")
        else:
            print(f"--- Feed for {username} ---")
            for post in posts:
                if post["author"] in following_list:
                    print(f"Author: {post['author']}")
                    print(f"Content: {post['content']}")
                    print(f"Likes: {post['likes']}\n")

def like_post(username, post_id_input):
    if username not in users:
        print(f"Error: User '{username}' does not exist!")
    else:
        post_id_input = int(post_id_input)
        post_found = False
        for post in posts:
            if post["id"] == post_id_input:
                post_found = True
                if post_id_input in users[username]["liked_posts"]:
                    print(f"Error: {username} has already liked post {post_id_input}!")
                else:
                    users[username]["liked_posts"].append(post_id_input)
                    post["likes"] += 1
                    print(f"{username} liked post {post_id_input}!")
                break
        if not post_found:
            print(f"Error: Post {post_id_input} does not exist!")

def follow_user(username, target):
    if username not in users:
        print(f"Error: User '{username}' does not exist!")
    elif target not in users:
        print(f"Error: User '{target}' does not exist!")
    elif username == target:
        print(f"Error: You cannot follow yourself!")
    elif target in users[username]["following"]:
        print(f"Error: {username} is already following {target}!")
    else:
        users[username]["following"].append(target)
        users[target]["followers"].append(username)
        print(f"{username} is now following {target}!")

def delete_post(username, post_id_input):
    post_id_input = int(post_id_input)
    
    # Step 1: Check if user exists
    if username not in users:
        print(f"Error: User '{username}' does not exist!")
        return
    
    post_found = False
    for post in posts:
        if post["id"] == post_id_input:
            post_found = True
           
            if post["author"] == username:
                posts.remove(post)
                print(f"Post {post_id_input} has been deleted!")
            else:
                print(f"Error: You are not the author of this post!")
            break
    
    # Step 4: If post wasn't found
    if not post_found:
        print(f"Error: Post {post_id_input} does not exist!")

def homemenu():
    while True:
        print('--- Mini Twitter Menu ---')
        print('1. create a new user')
        print('2. create a post')
        print('3. view feed')
        print('4. like a post')
        print('5. follow a user')
        print('6. delete a post')
        print('7. exit')
        choice = input('Select an option (1-7):').strip()
        if choice == '1':
            username = input('Enter username: ').strip()
            email = input('Enter email: ').strip()
            create_user(username, email)
        elif choice == '2':
            username = input('Enter username: ').strip()
            content = input('Enter post content: ').strip()
            create_post(username, content)
        elif choice == '3':
            username = input('Enter username: ').strip()
            view_feed(username)
        elif choice == '4':
            username = input('Enter username: ').strip()
            post_id_input = input('Enter post ID to like: ').strip()
            like_post(username, post_id_input)
        elif choice == '5':
            username = input('Enter username: ').strip()
            target = input('Enter username to follow: ').strip()
            follow_user(username, target)
        elif choice =='6':
            username = input('Enter username: ').strip()
            post_id_input = input('Enter post ID to delete: ').strip()
            delete_post(username, post_id_input)
        elif choice == '7':
            print('Goodbye!')
            break
        else:
                print("invalid choice. Select opitions 1-7.")
homemenu()
