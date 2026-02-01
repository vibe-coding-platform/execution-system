-- Within same DB transaction as business update:
INSERT INTO outbox_events (id, aggregate_type, aggregate_id, event_type, payload)
VALUES (
    gen_random_uuid(),
    'User',
    :user_id,
    'UserRegistered',
    jsonb_build_object(
        'userId', :user_id,
        'email', :email,
        'sourceSystem', 'auth-service'
    )
);

