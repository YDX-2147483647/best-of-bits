<!-- markdownlint-disable MD024 -->
# 贡献者指南

感谢你为本项目付出宝贵时间！

下面会介绍本项目如何组织，想更改时应该怎样操作。

> [!NOTE]
>
> 下面大多只是指导性建议；如果你知道自己想做什么，跟着感觉走即可。

## 新增项目

若要添加新项目，有如下两种方法。

- 提请修改（更简单）：

  1. 访问[议题页面](https://github.com/YDX-2147483647/best-of-bits/issues/new/choose)，选择类别，填写信息。

  2. 讨论充分后（或者你认为没必要讨论），评论`/draft-pr`，会[自动创建拉取请求](.github/workflows/add-project.yml)。

- 直接编辑（更自由）：在[`projects.yaml`](https://github.com/YDX-2147483647/best-of-bits/edit/main/projects.yaml)中增减项目，然后提交拉取请求。（可[直接用 GitHub UI 操作](https://github.com/YDX-2147483647/best-of-bits/edit/main/projects.yaml)）

提交议题、拉取请求前有如下常见问题。

- 请确保这一项目尚未被收录，而且还没有其他人请求。

    已收录的项目在 [projects.yaml](https://github.com/YDX-2147483647/best-of-bits/blob/main/projects.yaml)、[README.md](https://github.com/YDX-2147483647/best-of-bits/blob/main/README.md) 两个文件，其他人的请求在[议题](https://github.com/YDX-2147483647/best-of-bits/issues?q=is%3Aopen+label%3Aadd-project)，都可以搜索。

- 不要直接改`README.md`，而是改`projects.yaml`。

    `README.md`内容是每周 [GitHub Actions](https://github.com/YDX-2147483647/best-of-bits/actions/workflows/update-best-of-list.yml) 自动生成的，不用直接编辑。

- `projects.yaml`采用 [YAML](https://quickref.me/yaml) 格式，内容见[项目属性](#项目属性)一节。

    下面是个例子，可照猫画虎。

    ```yaml
    - name: BIT101
      homepage: https://bit101.cn
      github_id: flwfdd/BIT101
      category: website
      labels: [Web, python]
    ```

- 如果要添加好几个独立的项目，请分成多个议题／拉取请求。

- 议题、拉取请求的标题请以“新增项目：”开头。

    直接使用模板即可。

- 如果项目哪类也不算，`category`（类别）请写“杂项”（misc）。

    另外可以[新建议题](https://github.com/YDX-2147483647/best-of-bits/issues/new/choose)添加类别。

## 更改项目

若要更改现有项目，有如下两种方法。（和[新增项目](#新增项目)一样）

- 提请修改：访问[议题页面](https://github.com/YDX-2147483647/best-of-bits/issues/new/choose)，选择类别，填写信息。
- 直接编辑：在[`projects.yaml`](https://github.com/YDX-2147483647/best-of-bits/edit/main/projects.yaml)中增减项目，然后提交拉取请求。（可[直接用 GitHub UI 操作](https://github.com/YDX-2147483647/best-of-bits/edit/main/projects.yaml)）

提交议题、拉取请求前有如下常见问题。

- 不要直接改`README.md`，而是改`projects.yaml`。

- `projects.yaml`采用 [YAML](https://quickref.me/yaml) 格式，内容见[项目属性](#项目属性)一节。

- 如果要添加好几个独立的项目，请分成多个议题／拉取请求。

- 议题、拉取请求的标题请以“更改项目：”开头。

## 项目属性

> [!NOTE]
>
> 最新完整列表请参考 [best-of-generator 文档](https://github.com/best-of-lists/best-of-generator#project-properties)或[我们克隆的版本](https://github.com/YDX-2147483647/best-of-generator/tree/best-of-bits)。

<table>
    <thead>
        <tr>
            <th>属性</th>
            <th>描述</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>name</code></td>
            <td>项目名称。必须和其它项目不同。</td>
        </tr>
        <tr>
            <td><code>github_id</code></td>
            <td>GitHub ID，由作者名（或组织名）、仓库名组成，例如<code>best-of-lists/best-of-generator</code>。</td>
        </tr>
        <tr>
            <td><code>gitee_id</code></td>
            <td>Gitee ID，格式同<code>github_id</code></td>
        </tr>
        <tr>
            <td><code>greasy_fork_id</code></td>
            <td>Greasy Fork ID，是 URL 中的数字，例如<code>https://greasyfork.org/scripts/299792458-speed-of-light</code>中的<code>299792458</code>。</td>
        </tr>
        <tr>
            <td colspan="2"><strong>可选属性：</strong></td>
        </tr>
        <tr>
            <td><code>category</code></td>
            <td>类别的 ID。若项目涉及好几类，请只写最相关的那一类。具体 ID
                请参考<code>projects.yaml</code>里的<code>categories</code>。若不填，则会归入“Others”。</td>
        </tr>
        <tr>
            <td><code>labels</code></td>
            <td>项目相关的标签的列表。具体 ID
                请参考<code>projects.yaml</code>里的<code>labels</code>。</td>
        </tr>
        <tr>
            <td colspan="2"><strong>支持的包管理器：</strong></td>
        </tr>
        <tr>
            <td><code>pypi_id</code></td>
            <td>Python Package Index（<a href="https://pypi.org">PyPI</a>）上的项目 ID。</td>
        </tr>
        <tr>
            <td><code>conda_id</code></td>
            <td><a href="https://anaconda.org">Conda package manager</a> 上的项目 ID。如果主包在别的 channel，要前缀 channel，比如 <code>conda-forge/tensorflow</code>。</td>
        </tr>
        <tr>
            <td><code>npm_id</code></td>
            <td>Node package manager（<a href="https://www.npmjs.com">npm</a>）上的项目 ID。</td>
        </tr>
        <tr>
            <td><code>dockerhub_id</code></td>
            <td><a href="https://hub.docker.com">Docker Hub container registry</a> 上的项目 ID。</td>
        </tr>
        <tr>
            <td><code>maven_id</code></td>
            <td><a href="https://mvnrepository.com">Maven central</a> 上的 artifact ID，例如<code>org.apache.flink:flink-core</code>。</td>
        </tr>
    </tbody>
</table>

## 方针

### 收录标准

一言以蔽之：都收！

可行性：归功于 best-of 的自动排序，高质量项目会排到前面，长期不活跃的项目会被折叠隐藏。

意义：排除偏见，广而告之，考古指南，互帮互助，……

### 如何收录 monorepo 型项目

- `name`请用` ➡️ `分隔，例如`Batch_Collections ➡️ Campus_network`。
- 必须提供`description`。默认爬取的描述是整个仓库的描述，提供`description`可以人为指定，覆盖这一行为。
- `github_id`仍写整个仓库的。

## 上游项目

除了项目，本列表还涉及收集元数据、生成 markdown 等。这方面的贡献请移步 [best-of-generator](https://github.com/best-of-lists/best-of-generator) 仓库或我们克隆的 [best-of-update-action](https://github.com/YDX-2147483647/best-of-update-action/tree/ascii-description) 仓库。

若您想自己创建一个 best-of list，请参考[官方教程](https://github.com/best-of-lists/best-of/blob/main/create-best-of-list.md)，大概[需要三分钟](https://xkcd.com/2767/)。完成后 GitHub Actions 可以自动运行 best-of-generator。

## 贡献者公约

参与此项目即代表遵守[贡献者公约](https://github.com/YDX-2147483647/best-of-bits/blob/main/.github/CODE_OF_CONDUCT.md)。相互尊重才有我们才能合作干实事。辱骂、骚扰或其他不可接受的行为可向社区监督人报告。
