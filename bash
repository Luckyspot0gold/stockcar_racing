# Check notification status
gh api /notifications

# Mark all as read
gh api /notifications -X PUT -F "read=true"

# Disable email for a repo
gh api /repos/{owner}/{repo}/subscription -X PUT -F "ignored=true"
