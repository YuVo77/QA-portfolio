# 📄 Test Summary Report – Magento Demo Store

## 🔎 Project Name:
Magento Demo Store QA Testing

## 🧪 Test Type:
Manual Functional Testing (Web UI)

## 📅 Test Period:
June 2–6, 2025

## 👨‍💻 Tester:
Volodymyr

---

## ✅ Test Execution Summary (Grouped by Module)

### 1. 👤 User Registration
| Test Case ID | Title                                | Status   | Comments                                                                                     |
|--------------|--------------------------------------|----------|----------------------------------------------------------------------------------------------|
| TS01         | Register with valid user data        | ❌ Failed | This message may confuse a new user, as it lacks clear options (e.g., link to login or reset password).     |
| TS02         | Register with invalid email          | ✅ Passed | Proper validation message displayed.                                                         |
| TS03         | Register with existing email         | ✅ Passed | Duplicate email prevented correctly.                                                         |

---

### 2. 🔐 Login Functionality
| Test Case ID | Title                                | Status   | Comments                                                                                     |
|--------------|--------------------------------------|----------|----------------------------------------------------------------------------------------------|
| TS04         | Successful login with valid credential | ❌ Failed | User cannot log in despite providing correct credentials. This blocks access and indicates a possible bug in authentication or user status. |
| TS05         | Login with incorrect password        | ❌ Failed | The error message is too generic or misleading for wrong credentials. It may suggest account lockout, confusing users.                     |
| TS06         | Login with empty fields              | ✅ Passed | Validation works correctly; user prevented from submitting empty form.                       |

---

### 3. 🛒 Shopping Cart
| Test Case ID | Title                                | Status   | Comments                                                                                     |
|--------------|--------------------------------------|----------|----------------------------------------------------------------------------------------------|
| TS07         | Add to cart as guest                 | ✅ Passed | Item added successfully to cart.                                                             |
| TS08         | Update item quantity                 | ✅ Passed | Quantity updated and total price correct.                                                    |
| TS09         | Cart persists on refresh             | ✅ Passed | Cart contents retained after page refresh.                                                   |

---

### 4. 💳 Checkout Process
| Test Case ID | Title                                | Status   | Comments                                                                                     |
|--------------|--------------------------------------|----------|----------------------------------------------------------------------------------------------|
| TS10         | Complete checkout                    | ❌ Failed | The user is unexpectedly logged out or rejected during checkout, making it impossible to place the order despite a valid login session. This blocks the core functionality of the platform for registered users.              |
| TS11         | Missing shipping info                | ✅ Passed | Proper warning message displayed when shipping info is missing.                              |

---

### 5. 🔍 Product Search
| Test Case ID | Title                                | Status   | Comments                                                                                     |
|--------------|--------------------------------------|----------|----------------------------------------------------------------------------------------------|
| TS12         | Product search                       | ✅ Passed | Search results correctly matched input query.                                                |

---

## 📊 Overall Result:
**8 Passed, 4 Failed** – Critical issues found in registration, login, and checkout flows. These must be fixed before release.

---

### TS01 – Register with valid data
- This message may confuse new users, as it lacks clear options such as a link to login or reset password.  
- Recommend adding clear next steps or redirect to login page.

### TS04 – Login with valid credentials
- User cannot log in despite providing correct credentials, blocking access.  
- Possible bug in authentication or user status. Recommend investigating backend and user account status.

### TS05 – Login with incorrect password
- Error message is too generic or misleading for wrong credentials.  
- May suggest account lockout and confuse users. Improve error messaging clarity.

### TS10 – Checkout process failure
- User is unexpectedly logged out or rejected during checkout despite valid login session.  
- Blocks core functionality for registered users. Recommend fixing session management and authorization during checkout.
  
---

## 📋 Checklist Review Summary:

All functional checklists were filled and verified.  
✅ **All checklist items passed** – including validations, field visibility, and user interaction flows.

---

## 📎 Attachments:
- Screenshots of failed test scenarios  
- Authentication, registration, and checkout logs  
- Bug reports filed for TS01, TS04, TS05, and TS10

---
