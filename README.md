# Singularity HPC Registry

This is the main remote registry for [Singularity HPC](https://github.com/singularityhub/singularity-hpc).

[![DOI](https://zenodo.org/badge/519896622.svg)](https://zenodo.org/badge/latestdoi/519896622)

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

### Updates

Note that all of these scripts registry singularity-hpc (shpc) to be installed:

```bash
$ pip install singularity-hpc
```

#### Aliases

If you find a container missing aliases (or having extras) and you don't want to manually open files,
we provide a helper script to do so. After cloning the repository, you could check out a new branch and add an alias 
(note the `--registry` defaults to the present working directory where you are running the script, so this
should be run in the root of the cloned repository):

```bash
$ python .github/scripts/alias.py add quay.io/biocontainers/samtools test /opt/bin/test
```

If you ask to add an alias that already exists, this might mean changing the path, and you need to
use force:

```bash
$ python .github/scripts/alias.py add quay.io/biocontainers/samtools test /opt/bin/test --force
```

And then to remove:

```bash
$ python .github/scripts/alias.py remove quay.io/biocontainers/samtools test
```

If an alias doesn't exist, you will get an error on remove.
After these changes you would want to open a pull request to persist your changes to the registry.

#### Features

The equivalent helper exists for features. As an example, here is how to set a boolean
(true/false) or value of None):

```bash
$ python .github/scripts/feature.py add quay.io/biocontainers/samtools home true
$ python .github/scripts/feature.py add quay.io/biocontainers/samtools home false
$ python .github/scripts/feature.py add quay.io/biocontainers/samtools home none
```

And how to remove it:

```bash
$ python .github/scripts/feature.py remove quay.io/biocontainers/samtools home
```

And then to remove:

```bash
$ python .github/scripts/alias.py remove quay.io/biocontainers/samtools test /opt/bin/test
```

The same rule applies for using `--force`.

#### Environment

And finally, we have the same for environment. Here are examples:

```bash
$ python .github/scripts/env.py add quay.io/biocontainers/samtools maintainer vsoch
$ python .github/scripts/env.py remove quay.io/biocontainers/samtools maintainer
```

### BioContainers

We have a [script](.github/scripts/update_biocontainers.py) that will generate (non existing) modules for BioContainers,
and it is run once a week! It works by way of using an updated cache at [https://github.com/singularityhub/shpc-registry-cache]
generated directly from Biocontainers, which not only captures aliases for a latest tag, but also derives the accumulated
counts across all 8K+ containers. With these counts we can generate aliases as follows:

- Start with the loaded global counts, counts.json
- Subset to those in a container, the alias counts
- Rank ordering from least to greatest (lower frequency is a more unique commands we are interested in) 
- Including any counts with a frequency <= 10 (this accounts for containers with many unique aliases) `--min-count-inclusion`
- Above that threshold, including the next N `--additional-count-inclusion` (less unique but possibly important or interesting)
- Use these to generate a new container.yaml for the file (if it does not exist yet!)

To run the above, you'll need the cache cloned locally, and singularity-hpc installed

```bash
$ pip install git+https://github.com/singularityhub/singularity-hpc@main
$ pip install requests pipelib beautifulsoup4
$ git clone https://github.com/singularityhub/shpc-registry-cache /tmp/cache
```

And then to run the script (this shows the defaults)

```bash
$ python .github/scripts/update_biocontainers.py --cache /tmp/cache --registry $(pwd) --min-count-inclusion 10 --additional-count-inclusion 25
```

from the root. Since this added over 8K containers to the registry, we needed a new strategy for running the updater TBA!


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
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://vsoch.github.io"><img src="https://avatars.githubusercontent.com/u/814322?v=4?s=100" width="100px;" alt="Vanessasaurus"/><br /><sub><b>Vanessasaurus</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=vsoch" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/audreystott"><img src="https://avatars.githubusercontent.com/u/43943628?v=4?s=100" width="100px;" alt="Audrey Stott"/><br /><sub><b>Audrey Stott</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=audreystott" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="alecbcs.com"><img src="https://avatars.githubusercontent.com/u/19558067?v=4?s=100" width="100px;" alt="Alec Scott"/><br /><sub><b>Alec Scott</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=alecbcs" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/manbat"><img src="https://avatars.githubusercontent.com/u/41646490?v=4?s=100" width="100px;" alt="manbat"/><br /><sub><b>manbat</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=manbat" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/marcodelapierre"><img src="https://avatars.githubusercontent.com/u/16972180?v=4?s=100" width="100px;" alt="Marco De La Pierre"/><br /><sub><b>Marco De La Pierre</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=marcodelapierre" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://surak.wordpress.com"><img src="https://avatars.githubusercontent.com/u/878399?v=4?s=100" width="100px;" alt="Alexandre Strube"/><br /><sub><b>Alexandre Strube</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=surak" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/xdelaruelle"><img src="https://avatars.githubusercontent.com/u/4928853?v=4?s=100" width="100px;" alt="Xavier Delaruelle"/><br /><sub><b>Xavier Delaruelle</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=xdelaruelle" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/SarahBeecroft"><img src="https://avatars.githubusercontent.com/u/16343767?v=4?s=100" width="100px;" alt="SarahBeecroft"/><br /><sub><b>SarahBeecroft</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=SarahBeecroft" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://muffato.github.io"><img src="https://avatars.githubusercontent.com/u/623458?v=4?s=100" width="100px;" alt="Matthieu Muffato"/><br /><sub><b>Matthieu Muffato</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=muffato" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/georgiastuart"><img src="https://avatars.githubusercontent.com/u/8276147?v=4?s=100" width="100px;" alt="Georgia Stuart"/><br /><sub><b>Georgia Stuart</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=georgiastuart" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dipietrantonio"><img src="https://avatars.githubusercontent.com/u/2136256?v=4?s=100" width="100px;" alt="Cristian Di Pietrantonio"/><br /><sub><b>Cristian Di Pietrantonio</b></sub></a><br /><a href="https://github.com/singularityhub/shpc-registry/commits?author=dipietrantonio" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->


## License

This code is licensed under the MPL 2.0 [LICENSE](LICENSE).
