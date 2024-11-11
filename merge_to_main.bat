@echo off
REM Get current branch name
for /f "tokens=*" %%i in ('git rev-parse --abbrev-ref HEAD') do set CURRENT_BRANCH=%%i

REM Check if the current branch is "preview"
if "%CURRENT_BRANCH%"=="preview" (
    echo You are on the preview branch.
) else (
    echo You are not on the preview branch. Current branch is %CURRENT_BRANCH%.
    exit 0
)

REM Pull the latest changes
call git pull
IF %errorlevel% NEQ 0 (
    echo ERROR-preview: pull
    exit 1
)

REM Switch to the main branch
call git checkout main
IF %errorlevel% NEQ 0 (
    echo ERROR-preview: checkout main
    exit 1
)

REM Pull the latest changes on the main branch
call git pull
IF %errorlevel% NEQ 0 (
    echo ERROR-main: pull
    exit 1
)

REM Merge preview into main
call git merge preview
IF %errorlevel% NEQ 0 (
    echo ERROR-main: merge preview
    exit 1
)

REM Push the merged changes
call git push
IF %errorlevel% NEQ 0 (
    echo ERROR-main: push
    exit 1
)

REM Switch back to the preview branch
call git checkout preview
IF %errorlevel% NEQ 0 (
    echo ERROR-main:: git checkout preview
    exit 1
)

echo Finish.
exit 0
