# Singularity HPC Registry

This is testing having a remote registry for [Singularity HPC](https://github.com/singularityhub/singularity-hpc) to use.

**under development**

📖️ Read the [documentation](https://singularity-hpc.readthedocs.io/en/latest/) 📖️
⭐️ Browse the [container module collection](https://singularityhub.github.io/shpc-registry/) ⭐️

## Contribution

This registry showcases Singularity HPC (shpc), and provides the default set of containers for its default registry.
Contributions are very much welcome, so please do submit a pull-request if you'd like more software to be added, or open an issue to request a new addition!

The documentation has an [introduction](https://singularity-hpc.readthedocs.io/en/latest/getting_started/developer-guide.html#writing-registry-entries) about registries, and explains how to organize the required files for a container entry.

### Automated generation

First of all, there is an automated way of getting most of the `container.yaml` written via GitHub magic 🎩 automation.

1. [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) of this repository.
2. Go to the Actions tab.
3. Select "Generate New Container" in the left-hand side menu.
4. Click the "Run workflow" dropdown on the right-hand side.
5. Fill in the name of the container you want to build a `container.yaml` for, as well as a URL and a description (both are mandatory fields). Leave the branch as `main`.
6. Hit the green "Run workflow" button, wait and marvel at the magic :sparkles: happening. The GitHub Action will automatically open a pull request with most of the `container.yaml` filled in for you. You can check the branch out, edit it further – in particular refine the list aliases.

### Expected content

Refer to the documentation for a list of the [`container.yaml` fields](https://singularity-hpc.readthedocs.io/en/latest/getting_started/developer-guide.html#registry-yaml-fields), especially the _required_ ones.
A pull-request that doesn't contain the required fields will have changes requested to add them.

This registry is only for container images freely available. We can't accept `container.yaml` for private or access-restricted containers.

Furthermore, consider the following tips when making the pull-request:

- Ideally, the container tags listed in `container.yaml` should be actual versions, not generic `latest`, `stable`, which tend to be moving targets. Remember that containers and Singularity HPC are there for reproducibility !
- The convention here is to put containers hosted on the Docker Hub at the top of the repository, e.g. [ruby](https://github.com/singularityhub/shpc-registry/tree/main/ruby), rather than in a `docker.io` sub-directory.
- By putting your name down as `author`, you accept you may be contacted to review further updates of the `container.yaml`

## 😁️ Contributors 😁️

We use the [all-contributors](https://github.com/all-contributors/all-contributors)
tool to generate a contributors graphic below.

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://vsoch.github.io"><img src="https://avatars.githubusercontent.com/u/814322?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Vanessasaurus</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=vsoch" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/audreystott"><img src="https://avatars.githubusercontent.com/u/43943628?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Audrey Stott</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=audreystott" title="Code">💻</a></td>
    <td align="center"><a href="alecbcs.com"><img src="https://avatars.githubusercontent.com/u/19558067?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alec Scott</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=alecbcs" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/manbat"><img src="https://avatars.githubusercontent.com/u/41646490?v=4?s=100" width="100px;" alt=""/><br /><sub><b>manbat</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=manbat" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/marcodelapierre"><img src="https://avatars.githubusercontent.com/u/16972180?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Marco De La Pierre</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=marcodelapierre" title="Code">💻</a></td>
    <td align="center"><a href="http://surak.wordpress.com"><img src="https://avatars.githubusercontent.com/u/878399?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alexandre Strube</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=surak" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/xdelaruelle"><img src="https://avatars.githubusercontent.com/u/4928853?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Xavier Delaruelle</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=xdelaruelle" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/SarahBeecroft"><img src="https://avatars.githubusercontent.com/u/16343767?v=4?s=100" width="100px;" alt=""/><br /><sub><b>SarahBeecroft</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=SarahBeecroft" title="Code">💻</a></td>
    <td align="center"><a href="https://muffato.github.io"><img src="https://avatars.githubusercontent.com/u/623458?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Matthieu Muffato</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=muffato" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/georgiastuart"><img src="https://avatars.githubusercontent.com/u/8276147?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Georgia Stuart</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=georgiastuart" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->


## License

This code is licensed under the MPL 2.0 [LICENSE](LICENSE).
