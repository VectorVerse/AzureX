# Contributing Guidelines

Thank you for considering contributing to this project! We welcome all contributions that help improve the project.

## How to Contribute

### 1. Fork the Repository
Start by forking the repo and cloning it to your local machine.

```bash
git clone https://github.com/your-username/your-fork.git
```

### 2. Create a Branch
Use a feature or fix-specific branch name. **Always branch from `development`.**

```bash
git checkout development
git pull
git checkout -b feature/your-feature-name
```

### 3. Write Clean Code
- Follow the existing coding style and standards
- Keep your code clean, readable, and modular
- Add comments where necessary
- Write meaningful commit messages

### 4. Add Documentation
If your contribution changes any behavior, make sure to update relevant documentation, including README or inline comments.

### 5. Test Your Changes
Ensure your code is tested and does not break existing functionality.

### 6. Submit a Pull Request
Push your changes to your fork and open a pull request **into `development`**, not `main`. Provide a clear description of what you’ve done and why.

---

## 🔄 Branching Strategy

This project follows the **GitFlow workflow**:

- `main`: The stable, production-ready branch  
- `development`: Active development happens here; all feature branches are merged into this  
- `feature/*`: New features or enhancements should branch off from `development`  
- `bugFix/*`: New features or enhancements should branch off from `development`  
- `hotfix/*`: For urgent fixes based on `main`, if needed

#### 📌 Contribution Flow

1. **Branch off from `development`**:
   ```bash
   git checkout development
   git pull
   git checkout -b feature/your-feature-name
   ```
2. Make your changes
3. **Open a pull request** **into `development`**, not `main`

---

## 🧑‍💻 Naming Conventions

To maintain consistency in the codebase, please follow these naming conventions:

---

### 🐍 **snake_case**  
Used for **variables**, **functions**, and **methods**.

```python
# variable
user_name = "Alice"

# function
def get_user_data():
    return {"name": "Alice", "age": 30}

# method inside a class
class User:
    def get_full_name(self):
        return "Alice Johnson"
```

---

### 🏛 **PascalCase**  
Used for **class names**.

```python
class UserProfile:
    def __init__(self, name):
        self.name = name
```

---

### 🔠 **UPPERCASE**  
Used for **constants**.

```python
PI = 3.14159
MAX_USERS = 100
DEFAULT_TIMEOUT = 30
```


---

## Best Practices

- Keep pull requests small and focused  
- Use descriptive commit messages  
- Link to related issues or feature requests when possible  
- Be respectful and open to feedback during reviews

---

## Need Help?

If you have any questions or need clarification, feel free to open an issue or contact the maintainers.

Thanks for helping improve the project! 🙌
