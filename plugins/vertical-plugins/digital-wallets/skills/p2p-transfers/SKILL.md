---
name: p2p-transfers
description: |
  Peer-to-peer payment transfers between wallet users.
  Perfect for: person-to-person payments, split bills, request money, social payments.
  Not ideal for: merchant payments (use transaction-lifecycle), bulk payouts.
---

# P2P Transfers

## Core Philosophy
**"Sending money should be as easy as sending a message — instant, social, and free."**

## Transfer Types

### Send Money
1. Sender selects recipient (phone, email, username, QR code)
2. Enter amount and optional memo
3. Authenticate (PIN, biometric, or device trust)
4. Execute: debit sender wallet, credit recipient wallet
5. Both parties receive push notification

### Request Money
1. Requester creates payment request
2. Recipient receives notification with accept/decline option
3. On accept: execute as standard send from recipient
4. Request expires after 7 days (configurable)

### Split Bill
1. Initiator enters total amount
2. Select participants and split method:
   - **Equal**: Divide evenly
   - **Custom**: Set individual amounts
   - **Percentage**: Set individual percentages
   - **Itemized**: Assign menu items to individuals
3. Send requests to all participants
4. Track acceptance and payment status

## Recipient Resolution
| Input | Resolution |
|-------|-----------|
| Phone number | Look up by verified phone |
| Email address | Look up by verified email |
| Username | Direct wallet lookup |
| QR code | Decode wallet ID from QR |
| NFC tap | Read wallet ID from device NFC |

### Non-Registered Recipients
- If recipient doesn't have a wallet: send invitation link
- Funds held in escrow for 14 days
- After 14 days: auto-refund to sender

## Limits & Fees
| Transfer Type | Limit | Fee |
|---------------|-------|-----|
| Wallet-to-wallet | $5,000/day | Free |
| Send to non-user | $1,000/day | Free |
| Request money | $5,000/request | Free |
| International P2P | $2,500/day | 2.5% FX markup |

## Social Features
- Transaction feed (privacy-controlled)
- Payment memos and emoji reactions
- Group payment history
- Favorite contacts
- Payment reminders for pending requests
