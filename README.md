# Release

[GitHub 仓库](https://github.com/4ucl/scripts)配置了 tag 触发自动打包发布。 

```bash
# 删除本地仓库 tag（如有）
git tag -d v1.0.0
# 推送删除操作到远程仓库
git push origin :refs/tag/v1.0.0
# 在本地仓库创建新 tag
git tag -a v1.0.0 -m "Tag v1.0.0"
# 推送新 tag 到远程仓库
git push origin v1.0.0
```