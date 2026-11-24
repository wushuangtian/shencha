import sys
import review_delivery
if __name__ == '__main__':
    try:
        sys.exit(review_delivery.main())
    except Exception as exc:
        print(f'交付未确认成功（{type(exc).__name__}），请检查收件箱，避免重发。', file=sys.stderr)
        sys.exit(1)
