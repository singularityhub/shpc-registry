---
layout: container
name:  "quay.io/biocontainers/rsat-core"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rsat-core/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/rsat-core/container.yaml"
updated_at: "2022-10-27 00:34:09.402455"
latest: "2020.02.29--py36pl526r36hc99cbb1_0"
container_url: "https://biocontainers.pro/tools/rsat-core"
aliases:
 - ".vmatch-post-link.sh"
 - ".vmatch-pre-unlink.sh"
 - "Vmatchtrans.pl"
 - "bigWigToWig.pl"
 - "chain2dim"
 - "cleanpp.sh"
 - "compare-matrices-quick"
 - "count-words"
 - "cpp"
 - "index_bigwigset.pl"
 - "info-gibbs"
 - "lz4_decompress"
 - "matchcluster"
 - "matrix-scan-quick"
 - "mkdna6idx"
 - "mkvtree"
 - "mysql.server"
 - "mysql_client_test_embedded"
 - "mysql_config_editor"
 - "mysql_embedded"
 - "mysql_install_db"
 - "mysql_ssl_rsa_setup"
 - "mysqlpump"
 - "mysqltest_embedded"
 - "mysqlxtest"
 - "repfind.pl"
 - "retrieve-variation-seq"
 - "rsat"
 - "upgradeprj.pl"
 - "variation-scan"
 - "vendian"
 - "vmatch"
 - "vmatchselect"
 - "vmigrate.sh"
 - "vseqinfo"
 - "vseqselect"
 - "vstree2tex"
 - "vsubseqselect"
 - "wigToBigWig.pl"
 - "zlib_decompress"
versions:
 - "2020.02.29--py36pl526r36hc99cbb1_0"
description: "shpc-registry automated BioContainers addition for rsat-core"
config: {"url": "https://biocontainers.pro/tools/rsat-core", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rsat-core", "latest": {"2020.02.29--py36pl526r36hc99cbb1_0": "sha256:6c033b4da5fa279ef7139b6614a1e6f95f725a3cffffc12b4cbf8c2260313402"}, "tags": {"2020.02.29--py36pl526r36hc99cbb1_0": "sha256:6c033b4da5fa279ef7139b6614a1e6f95f725a3cffffc12b4cbf8c2260313402"}, "docker": "quay.io/biocontainers/rsat-core", "aliases": {".vmatch-post-link.sh": "/usr/local/bin/.vmatch-post-link.sh", ".vmatch-pre-unlink.sh": "/usr/local/bin/.vmatch-pre-unlink.sh", "Vmatchtrans.pl": "/usr/local/bin/Vmatchtrans.pl", "bigWigToWig.pl": "/usr/local/bin/bigWigToWig.pl", "chain2dim": "/usr/local/bin/chain2dim", "cleanpp.sh": "/usr/local/bin/cleanpp.sh", "compare-matrices-quick": "/usr/local/bin/compare-matrices-quick", "count-words": "/usr/local/bin/count-words", "cpp": "/usr/local/bin/cpp", "index_bigwigset.pl": "/usr/local/bin/index_bigwigset.pl", "info-gibbs": "/usr/local/bin/info-gibbs", "lz4_decompress": "/usr/local/bin/lz4_decompress", "matchcluster": "/usr/local/bin/matchcluster", "matrix-scan-quick": "/usr/local/bin/matrix-scan-quick", "mkdna6idx": "/usr/local/bin/mkdna6idx", "mkvtree": "/usr/local/bin/mkvtree", "mysql.server": "/usr/local/bin/mysql.server", "mysql_client_test_embedded": "/usr/local/bin/mysql_client_test_embedded", "mysql_config_editor": "/usr/local/bin/mysql_config_editor", "mysql_embedded": "/usr/local/bin/mysql_embedded", "mysql_install_db": "/usr/local/bin/mysql_install_db", "mysql_ssl_rsa_setup": "/usr/local/bin/mysql_ssl_rsa_setup", "mysqlpump": "/usr/local/bin/mysqlpump", "mysqltest_embedded": "/usr/local/bin/mysqltest_embedded", "mysqlxtest": "/usr/local/bin/mysqlxtest", "repfind.pl": "/usr/local/bin/repfind.pl", "retrieve-variation-seq": "/usr/local/bin/retrieve-variation-seq", "rsat": "/usr/local/bin/rsat", "upgradeprj.pl": "/usr/local/bin/upgradeprj.pl", "variation-scan": "/usr/local/bin/variation-scan", "vendian": "/usr/local/bin/vendian", "vmatch": "/usr/local/bin/vmatch", "vmatchselect": "/usr/local/bin/vmatchselect", "vmigrate.sh": "/usr/local/bin/vmigrate.sh", "vseqinfo": "/usr/local/bin/vseqinfo", "vseqselect": "/usr/local/bin/vseqselect", "vstree2tex": "/usr/local/bin/vstree2tex", "vsubseqselect": "/usr/local/bin/vsubseqselect", "wigToBigWig.pl": "/usr/local/bin/wigToBigWig.pl", "zlib_decompress": "/usr/local/bin/zlib_decompress"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rsat-core.
shpc-registry automated BioContainers addition for rsat-core
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rsat-core
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rsat-core:2020.02.29--py36pl526r36hc99cbb1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rsat-core/2020.02.29--py36pl526r36hc99cbb1_0
$ module help quay.io/biocontainers/rsat-core/2020.02.29--py36pl526r36hc99cbb1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rsat-core-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rsat-core-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rsat-core-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rsat-core-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rsat-core-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rsat-core-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .vmatch-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.vmatch-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.vmatch-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.vmatch-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .vmatch-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.vmatch-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.vmatch-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.vmatch-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Vmatchtrans.pl

```bash
$ singularity exec <container> /usr/local/bin/Vmatchtrans.pl
$ podman run --it --rm --entrypoint /usr/local/bin/Vmatchtrans.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Vmatchtrans.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bigWigToWig.pl

```bash
$ singularity exec <container> /usr/local/bin/bigWigToWig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bigWigToWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bigWigToWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chain2dim

```bash
$ singularity exec <container> /usr/local/bin/chain2dim
$ podman run --it --rm --entrypoint /usr/local/bin/chain2dim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chain2dim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cleanpp.sh

```bash
$ singularity exec <container> /usr/local/bin/cleanpp.sh
$ podman run --it --rm --entrypoint /usr/local/bin/cleanpp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cleanpp.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compare-matrices-quick

```bash
$ singularity exec <container> /usr/local/bin/compare-matrices-quick
$ podman run --it --rm --entrypoint /usr/local/bin/compare-matrices-quick   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare-matrices-quick   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### count-words

```bash
$ singularity exec <container> /usr/local/bin/count-words
$ podman run --it --rm --entrypoint /usr/local/bin/count-words   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/count-words   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpp

```bash
$ singularity exec <container> /usr/local/bin/cpp
$ podman run --it --rm --entrypoint /usr/local/bin/cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index_bigwigset.pl

```bash
$ singularity exec <container> /usr/local/bin/index_bigwigset.pl
$ podman run --it --rm --entrypoint /usr/local/bin/index_bigwigset.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index_bigwigset.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### info-gibbs

```bash
$ singularity exec <container> /usr/local/bin/info-gibbs
$ podman run --it --rm --entrypoint /usr/local/bin/info-gibbs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/info-gibbs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lz4_decompress

```bash
$ singularity exec <container> /usr/local/bin/lz4_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/lz4_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lz4_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matchcluster

```bash
$ singularity exec <container> /usr/local/bin/matchcluster
$ podman run --it --rm --entrypoint /usr/local/bin/matchcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matchcluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### matrix-scan-quick

```bash
$ singularity exec <container> /usr/local/bin/matrix-scan-quick
$ podman run --it --rm --entrypoint /usr/local/bin/matrix-scan-quick   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/matrix-scan-quick   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkdna6idx

```bash
$ singularity exec <container> /usr/local/bin/mkdna6idx
$ podman run --it --rm --entrypoint /usr/local/bin/mkdna6idx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkdna6idx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkvtree

```bash
$ singularity exec <container> /usr/local/bin/mkvtree
$ podman run --it --rm --entrypoint /usr/local/bin/mkvtree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkvtree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql.server

```bash
$ singularity exec <container> /usr/local/bin/mysql.server
$ podman run --it --rm --entrypoint /usr/local/bin/mysql.server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql.server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_client_test_embedded

```bash
$ singularity exec <container> /usr/local/bin/mysql_client_test_embedded
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_client_test_embedded   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_client_test_embedded   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config_editor

```bash
$ singularity exec <container> /usr/local/bin/mysql_config_editor
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_config_editor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_config_editor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_embedded

```bash
$ singularity exec <container> /usr/local/bin/mysql_embedded
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_embedded   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_embedded   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_install_db

```bash
$ singularity exec <container> /usr/local/bin/mysql_install_db
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_install_db   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_install_db   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_ssl_rsa_setup

```bash
$ singularity exec <container> /usr/local/bin/mysql_ssl_rsa_setup
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_ssl_rsa_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_ssl_rsa_setup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlpump

```bash
$ singularity exec <container> /usr/local/bin/mysqlpump
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlpump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlpump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqltest_embedded

```bash
$ singularity exec <container> /usr/local/bin/mysqltest_embedded
$ podman run --it --rm --entrypoint /usr/local/bin/mysqltest_embedded   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqltest_embedded   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysqlxtest

```bash
$ singularity exec <container> /usr/local/bin/mysqlxtest
$ podman run --it --rm --entrypoint /usr/local/bin/mysqlxtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysqlxtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repfind.pl

```bash
$ singularity exec <container> /usr/local/bin/repfind.pl
$ podman run --it --rm --entrypoint /usr/local/bin/repfind.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repfind.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### retrieve-variation-seq

```bash
$ singularity exec <container> /usr/local/bin/retrieve-variation-seq
$ podman run --it --rm --entrypoint /usr/local/bin/retrieve-variation-seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/retrieve-variation-seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsat

```bash
$ singularity exec <container> /usr/local/bin/rsat
$ podman run --it --rm --entrypoint /usr/local/bin/rsat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### upgradeprj.pl

```bash
$ singularity exec <container> /usr/local/bin/upgradeprj.pl
$ podman run --it --rm --entrypoint /usr/local/bin/upgradeprj.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/upgradeprj.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### variation-scan

```bash
$ singularity exec <container> /usr/local/bin/variation-scan
$ podman run --it --rm --entrypoint /usr/local/bin/variation-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/variation-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vendian

```bash
$ singularity exec <container> /usr/local/bin/vendian
$ podman run --it --rm --entrypoint /usr/local/bin/vendian   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vendian   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vmatch

```bash
$ singularity exec <container> /usr/local/bin/vmatch
$ podman run --it --rm --entrypoint /usr/local/bin/vmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vmatchselect

```bash
$ singularity exec <container> /usr/local/bin/vmatchselect
$ podman run --it --rm --entrypoint /usr/local/bin/vmatchselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vmatchselect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vmigrate.sh

```bash
$ singularity exec <container> /usr/local/bin/vmigrate.sh
$ podman run --it --rm --entrypoint /usr/local/bin/vmigrate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vmigrate.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vseqinfo

```bash
$ singularity exec <container> /usr/local/bin/vseqinfo
$ podman run --it --rm --entrypoint /usr/local/bin/vseqinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vseqinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vseqselect

```bash
$ singularity exec <container> /usr/local/bin/vseqselect
$ podman run --it --rm --entrypoint /usr/local/bin/vseqselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vseqselect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vstree2tex

```bash
$ singularity exec <container> /usr/local/bin/vstree2tex
$ podman run --it --rm --entrypoint /usr/local/bin/vstree2tex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vstree2tex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsubseqselect

```bash
$ singularity exec <container> /usr/local/bin/vsubseqselect
$ podman run --it --rm --entrypoint /usr/local/bin/vsubseqselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsubseqselect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wigToBigWig.pl

```bash
$ singularity exec <container> /usr/local/bin/wigToBigWig.pl
$ podman run --it --rm --entrypoint /usr/local/bin/wigToBigWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wigToBigWig.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zlib_decompress

```bash
$ singularity exec <container> /usr/local/bin/zlib_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/zlib_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zlib_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)