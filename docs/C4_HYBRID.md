# C-4.1–C-4.3 PC + GitHub Actions

Windows는 후보와 원문 근거를 만들고, GitHub만 최종 공식 데이터를 게시한다. 기존 B 패키저·적용·복구·Ed25519 승인과 beta.30.7 데이터 ABI를 재사용한다. 프로그램/EXE·GUI·전투 계산식은 변경하지 않는다.

## 실행과 초기 운영 상태

- Windows: 기존 `RAID Champion DB C4 Data Updates` 작업, 6시간·로그인 복구 유지. 명령은 `tools/c4_hybrid.py local`. 공식 게시 불가.
- GitHub: `.github/workflows/c4-data.yml`, UTC 01:23/07:23/13:23/19:23(한국 04:23/10:23/16:23/22:23), `ubuntu-latest`, 25분 제한. `workflow_dispatch` 즉시 진단 가능. 정각 부하를 피한다.
- 공개 표준 실행기만 사용한다. 유료 서비스/Larger Runner/API·Actions 캐시·아티팩트 업로드 없음. 실행 로그와 요약은 GitHub 기본 보존 정책을 사용한다. 공유 ZIP은 각각 최대25MiB/펼친 내용200MiB로 제한한다.
- **최초 자동 게시 활성화 전** 저장소 변수 `C4_ENABLE_PUBLISH=false`. 감지·검증·AUTO_READY 패키징·체크포인트는 동작한다. 새 데이터 활성화/서명은 하지 않는다.
- 사용자 GUI 검수와 안전성 확인 후 최초 활성화를 별도 기록한다. 환경 `c4-production`의 `C4_SIGNING_KEY` Secret에 기존 키를 암호화 저장하고 공개 신뢰 키와 일치하는지 확인한 뒤 변수만 true로 바꾼다. 키를 소스/로그/ZIP에 넣지 않는다. 실제 키 전송과 이 변수 변경은 이번 초기 감시 설치에 포함하지 않는다. 이후 각 데이터 변경마다 사람 승인은 요구하지 않는다.

## PC 없이 가능한 범위

리뷰된 실행 코드와 게임 DB/ID 맵·기존52후보 및 해당 원문만 `automation/c4/runtime.zip`에 고정한다. `runtime.json`은 모든 파일 크기/SHA-256을 기록하며 bootstrap은 전체 검증 후 새 격리 디렉터리에만 펼친다. PC 경로/사용자 프로필/개인 JSON/Windows gh 실행파일/키가 필요하지 않다. Ubuntu Python3.12와 기존 cryptography만 사용한다.

C-1의 HTTP/robots/조건부 요청/DOM/챔피언·스킬 파서를 그대로 쓴다. 3개 감지 출처가 같으면 상세수집0. 변경이 있으면 기존 C-4의8 hero/40요청/15분 한도를 사용하고 중단 시 다음 실행에서 이어받는다. 사이트 차단/공식 근거 부족/신규 스키마 불완전은 보류하며 PC 부재를 추측으로 메우지 않는다.

실제 게임 효과·계수·강화/대상 전체의 의미 변환은 아직 지원하지 않는다. 현재41보류=신규5 hero의25필드+스킬7+메타데이터/이름9. 스킬7은 원문 URL/hero/skill ID와 원문 오브젝트/파생 필드를 다시 대조하고 운영 form/skill 연결·쿨타임을 확인한다. 임의 수치/한국어/최대스탯 생성 없음. 과거 Big Un/Brakus/Rhazin A3는1.0.1에 이미 반영되어 재게시하지 않는다.

## 공유·중복·복구

`c4-automation-state` 별도 브랜치의 `local.zip`은 허용된 후보 필드와 콘텐츠 주소 원문만 포함한다. readiness/gates/서명 키/개인 자료/코드 수신은 거부한다. 클라우드는 실제 원문과 현재 공식 공지를 다시 해석한다. 초기 후보 공유는 완전한 수집 커버리지를 주장하지 않아 필요한 상세수집을 생략하지 않는다.

`cloud.zip`은 클라우드의 처리 상태·선택 근거·원문·공식 기준 체크포인트다. 허용 경로/확장자/크기·중복 ZIP 항목을 검사하고 코드/키는 복원하지 않는다. 공식 데이터는 항상 현재 서명·SHA를 다시 검증한다. PC는 클라우드가 동일 출처 지문과 동일 공식 매니페스트를 이미 처리했으면 복잡한 재수집을 생략한다. 상태 브랜치 쓰기도 non-force 경합 검사와 최대3회 제한을 따른다. 출처/상태 변화가 없으면 상태 커밋을 만들지 않는다.

Actions concurrency와 로컬 OS 잠금은 각 환경에서만 유효하다. 환경 간에는 공유 지문/공식 버전, champion/hero/form/skill ID, 전후값/콘텐츠/패치 해시를 비교한다. 최종 게시 전 최신 공식 서명·매니페스트를 다시 읽고 non-force Git ref 갱신으로 경합을 거부한다. 활성 매니페스트·서명·처리 해시 원장을 한 커밋으로 기록한다. 로컬 직접 게시와 test_data 공식 게시를 거부한다.

게시 순서는 검증→B 패키징/격리 적용·복구→해시→기존 서명→불변 payload 업로드→익명 접근/바이트 확인→활성 쌍/처리 원장 마지막 갱신→최종 접근 확인이다. 실패 시 기존 활성 쌍 유지, 동일 실패3회 후 보류. AUTO_READY0이면 NO_UPDATE·버전 증가 없음. 같은 출처가 그대로면 NO_CHANGE.

## 설치된 프로그램

beta.30.7 기본 설정은 시작 시 서명된 최신 데이터 검사·다운로드·검증·적용을 자동 수행한다(기존6시간 쿨다운/사용자가 꺼둔 설정 존중). 실행 중 분석은 고정 snapshot을 유지하며 다음 정상 실행 시 새 세대를 사용한다. 강제 재시작·상시 실행 중 주기 검사 추가는 차기 EXE 범위다. 팀/보유/최종스탯/장비 개인 JSON과 Dropbox 데몬로드 원장은 수집·공유 대상이 아니다.

## 감시 확인 및 복구

```powershell
& 'scratch/step5/build_env/Scripts/python.exe' -X utf8 tools/c4_hybrid.py local
& 'scratch/auto_update_b/remote_review/github_cli/bin/gh.exe' workflow view c4-data.yml --repo dlckdtnr1212-lang/RAID-Champion-DB
& 'scratch/auto_update_b/remote_review/github_cli/bin/gh.exe' workflow run c4-data.yml --repo dlckdtnr1212-lang/RAID-Champion-DB
```

공개 저장소는60일 활동이 없으면 예약이 비활성화될 수 있고 부하 시 예약 지연/누락도 가능하다. PC 작업은 워크플로 실제 state를 기록한다. 비활성이면 `gh workflow enable c4-data.yml --repo ...` 후 workflow run으로 재개한다. PC와 예약 워크플로가 동시에 장기간 비활성이면 외부 유료 감시 없이 자동 복구를 보장할 수 없다. 활동 위장용 커밋을 만들지 않는다.

근거: [무료 표준 실행기/저장소 비용](https://docs.github.com/en/billing/concepts/product-billing/github-actions), [실행 한도](https://docs.github.com/en/actions/reference/limits), [예약 제한](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

상태는 IMPLEMENTED(구현), TESTED(격리·실행 시험), ACTIVATED(예약 감시), PUBLISHED(신규 공식 데이터), VERIFIED(사용자 설치본 새 공식 데이터 확인)를 구분한다. 감시 활성화는 최초 운영 자동 게시 활성화와 별도다.
