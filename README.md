# Release

[GitHub 仓库](https://github.com/4ucl/scripts)配置了 tag 触发自动打包发布。 

```bash
# 删除本地 tag（如有）
git tag -d v1.0.0
# 删除远程 tag
git push origin --delete v1.0.0
# 创建本地 tag
git tag -a v1.0.0 -m "Tag v1.0.0"
# 推送新 tag 到远程仓库
git push origin v1.0.0
```