# Third-party components

The Go2 model, meshes, example controller configuration, and pretrained
`go2_cts_150k.pt` policy are downloaded from
[wty-yy/go2_rl_lab](https://github.com/wty-yy/go2_rl_lab), pinned at commit
`24859ea57953624de8208ddc11b606ebfec5c99c`. The exact URLs and SHA-256 digests
are recorded in `assets.lock.json`. The downloaded upstream `LICENSE` is at
`assets/go2_rl_lab/LICENSE` and must accompany redistribution of those files.

The Python locomotion observation layout, PD gains and action scaling in
`go2_demo/backend.py` are adapted from that project's
`deploy/deploy_mujoco/deploy_go2.py` and `configs/go2.yaml`.

Upstream attribution: Copyright (c) 2025 Wu Tianyang, MIT License. The upstream
license also includes BSD 3-Clause attribution to Copyright (c) 2016–2023
HangZhou YuShu TECHNOLOGY CO., LTD. (Unitree Robotics). Preserve the complete
license text distributed with the assets. Dependencies such as MuJoCo,
PyTorch, NumPy and OpenCV retain their respective licenses.

This demo implements a small RGB-D navigation harness inspired by
[RoboHarness](https://github.com/BinceQu/RoboHarness). It does not copy that
project's robot tools and is not a reproduction of its BEHAVIOR experiments.

## Complete upstream license

```text
MIT License

Copyright (c) 2025 Wu Tianyang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

This project is based on or incorporates code from https://github.com/unitreerobotics/unitree_rl_gym,
which is licensed under the BSD 3-Clause License:

BSD 3-Clause License
Copyright (c) 2016-2023 HangZhou YuShu TECHNOLOGY CO.,LTD. ("Unitree Robotics")
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

```

## QUARD dataset samples

The optional offline regression samples are extracted from
[Tong314/QUARD](https://huggingface.co/datasets/Tong314/QUARD), the dataset linked
by the [official QUART-Online project](https://quart-online.github.io/) and
[repository](https://github.com/yuan48/QUART-Online). The source dataset is pinned
at Hugging Face revision `375cbd77d6b8e96ff82e1529f0c44caa5c182d5e`.

The published dataset card declares the MIT license. Preserve the source dataset
card, sample provenance and license information when redistributing the samples.
The upstream QUART-Online repository separately publishes an MIT license with
attribution `Copyright (c) 2025 Tong3143`; its pinned license is available at
[LICENSE](https://github.com/yuan48/QUART-Online/blob/da8a0d3c3c4e8663d414b952c078d29b4316b7c4/LICENSE).

The archive identities and extracted-file hashes are recorded in
`datasets/quard.lock.json`. Samples live under `data/quard/`. Only parts of the
source archives are read: the recorded full-archive hashes are provenance
metadata, not a claim that the complete source archives have been verified.

The local 15-task sample selection and four-frame windows are regression
fixtures chosen by this project. They are not the unreleased exact CerebVLA
training/evaluation split, its generated XML reasoning annotations, or its
real-world demonstrations. No CerebVLA model, QUART-Online weights or original
Isaac Gym runtime is installed by this dataset integration. See
[dataset documentation](docs/quard.md) for the sample schema and limitations.
