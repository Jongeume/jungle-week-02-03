#!/usr/bin/env python3
"""
알고리즘 학습 문제 채점 스크립트 (Week3 Advanced)

사용법:
  python check.py <문제파일명>          # 단일 문제 채점
  예: python check.py 01_topological_sort.py

  python check.py --all                # 모든 문제 한 번에 채점
  python check.py                      # (인자 없음) --all 과 동일하게 전체 채점
"""

import sys
import subprocess
import os
import re
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


def discover_problem_files():
    """현재 폴더의 'NN_*.py' 형식 문제 파일을 번호 순서대로 반환"""
    pattern = re.compile(r"^(\d{2})_.+\.py$")
    files = []
    for entry in SCRIPT_DIR.iterdir():
        if entry.is_file() and entry.name != "check.py":
            m = pattern.match(entry.name)
            if m:
                files.append((int(m.group(1)), entry.name))
    files.sort(key=lambda x: x[0])
    return [name for _, name in files]


def check_solution(problem_file):
    """
    문제 파일을 실행하고 정답과 비교

    Args:
        problem_file: 문제 파일명 (현재 폴더 기준 상대경로)

    Returns:
        (passed, message) 튜플
    """
    problem_path = SCRIPT_DIR / problem_file

    if not problem_path.exists():
        return False, f"❌ 파일을 찾을 수 없습니다: {problem_file}"

    base_name = problem_file.replace('.py', '')
    output_file = SCRIPT_DIR / f"{base_name}_output.txt"

    if not output_file.exists():
        return False, f"❌ 정답 파일을 찾을 수 없습니다: {output_file.name}"

    try:
        result = subprocess.run(
            ['python3', str(problem_path)],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=str(SCRIPT_DIR),
        )

        if result.returncode != 0:
            return False, f"❌ 실행 오류:\n{result.stderr}"

        actual_output = result.stdout.strip()

        with open(output_file, 'r', encoding='utf-8') as f:
            expected_output = f.read().strip()

        # 공백 정규화 후 비교
        actual_lines = [line.strip() for line in actual_output.split('\n') if line.strip()]
        expected_lines = [line.strip() for line in expected_output.split('\n') if line.strip()]

        if actual_lines == expected_lines:
            return True, "✅ PASS - 정답입니다!"
        else:
            diff_msg = "❌ FAIL - 출력이 다릅니다.\n\n"
            diff_msg += "=== 예상 출력 ===\n"
            diff_msg += expected_output[:500]
            if len(expected_output) > 500:
                diff_msg += "\n... (생략)"
            diff_msg += "\n\n=== 실제 출력 ===\n"
            diff_msg += actual_output[:500]
            if len(actual_output) > 500:
                diff_msg += "\n... (생략)"
            return False, diff_msg

    except subprocess.TimeoutExpired:
        return False, "❌ 시간 초과 (10초)"
    except Exception as e:
        return False, f"❌ 오류 발생: {str(e)}"


def run_all():
    problem_files = discover_problem_files()

    if not problem_files:
        print("⚠️  채점할 문제 파일을 찾지 못했습니다.")
        return 1

    print("=" * 60)
    print(f"Week3 Advanced 전체 문제 채점 (총 {len(problem_files)}개)")
    print("=" * 60)
    print()

    passed = 0
    failed = 0
    failed_files = []

    for problem_file in problem_files:
        print(f"📝 {problem_file}")
        success, message = check_solution(problem_file)

        if success:
            print(f"   {message}")
            passed += 1
        else:
            print(f"   {message.splitlines()[0]}")
            failed += 1
            failed_files.append(problem_file)
        print()

    print("=" * 60)
    print(f"결과: {passed}개 통과, {failed}개 실패 (총 {passed + failed}개)")
    if failed_files:
        print("실패한 문제:")
        for name in failed_files:
            print(f"  - {name}")
    print("=" * 60)

    return 0 if failed == 0 else 1


def run_single(problem_file):
    print("=" * 60)
    print(f"문제: {problem_file}")
    print("=" * 60)
    print()

    success, message = check_solution(problem_file)
    print(message)
    print()

    if success:
        print("🎉 축하합니다! 문제를 해결했습니다!")
        return 0
    else:
        print("💡 힌트: 문제 파일의 TODO 부분을 다시 확인해보세요.")
        return 1


def main():
    # 인자 없음 또는 --all 인 경우: 전체 채점
    if len(sys.argv) < 2 or sys.argv[1] == '--all':
        sys.exit(run_all())

    if sys.argv[1] in ('-h', '--help'):
        print(__doc__)
        return

    sys.exit(run_single(sys.argv[1]))


if __name__ == '__main__':
    main()
