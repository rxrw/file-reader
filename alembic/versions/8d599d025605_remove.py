"""remove 

Revision ID: 8d599d025605
Revises: 8effd1c19c35
Create Date: 2020-11-30 15:53:56.451886

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8d599d025605'
down_revision = '8effd1c19c35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_qiye_tel', table_name='qiye')
    op.drop_table('qiye')
    op.drop_index('ix_shunfeng_tel', table_name='shunfeng')
    op.drop_table('shunfeng')
    op.drop_index('ix_kfc_email', table_name='kfc')
    op.drop_index('ix_kfc_tel', table_name='kfc')
    op.drop_table('kfc')
    op.drop_index('ix_car_email', table_name='car')
    op.drop_index('ix_car_tel', table_name='car')
    op.drop_table('car')
    op.drop_index('ix_jiekuan_qq', table_name='jiekuan')
    op.drop_index('ix_jiekuan_tel', table_name='jiekuan')
    op.drop_table('jiekuan')
    op.drop_index('ix_qq_qq', table_name='qq')
    op.drop_index('ix_qq_tel', table_name='qq')
    op.drop_table('qq')
    op.drop_index('ix_pingan_email', table_name='pingan')
    op.drop_index('ix_pingan_tel', table_name='pingan')
    op.drop_table('pingan')
    op.drop_index('ix_gongan_tel', table_name='gongan')
    op.drop_table('gongan')
    op.drop_index('ix_weibo_tel', table_name='weibo')
    op.drop_index('ix_weibo_uid', table_name='weibo')
    op.drop_table('weibo')
    op.drop_index('ix_jingdong_mail', table_name='jingdong')
    op.drop_index('ix_jingdong_tel', table_name='jingdong')
    op.drop_table('jingdong')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jingdong',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('username', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('password_md5', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('mail', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('card_no', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('tel', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('phone', mysql.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_jingdong_tel', 'jingdong', ['tel'], unique=False)
    op.create_index('ix_jingdong_mail', 'jingdong', ['mail'], unique=False)
    op.create_table('weibo',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('uid', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('tel', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_weibo_uid', 'weibo', ['uid'], unique=False)
    op.create_index('ix_weibo_tel', 'weibo', ['tel'], unique=False)
    op.create_table('gongan',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('belong_station', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('create_time', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('address_available', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('code', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('birth', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('gender', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('card_no', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('tel', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('address', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('bm1', mysql.VARCHAR(length=4), nullable=True),
    sa.Column('bm2', mysql.VARCHAR(length=4), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_gongan_tel', 'gongan', ['tel'], unique=False)
    op.create_table('pingan',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('product_name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('money', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('duration', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('card_no', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('gender', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('tel', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('province', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('city', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('income', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('married', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('insure_form', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('insure_industy', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('insure_aim', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('fee_util', mysql.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_pingan_tel', 'pingan', ['tel'], unique=False)
    op.create_index('ix_pingan_email', 'pingan', ['email'], unique=False)
    op.create_table('qq',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('qq', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('tel', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_qq_tel', 'qq', ['tel'], unique=False)
    op.create_index('ix_qq_qq', 'qq', ['qq'], unique=False)
    op.create_table('jiekuan',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('amount', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('gender', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('native', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('card_util_date', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('card_no_place', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('card_no_address', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('address', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('wechat', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('qq', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('card_no', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('tel', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('education_level', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('married', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('sons', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('home_type', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('wife_name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('wife_card_no', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('wife_company', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('direct_namee', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('direct_relation', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('direct_tel', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('direct_address', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('company', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('department', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('duty', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('job_start_date', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('job_salary_date', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('month_outcome', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('month_income', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('job_initial_date', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('lend_time', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('company_property', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('birth', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_jiekuan_tel', 'jiekuan', ['tel'], unique=False)
    op.create_index('ix_jiekuan_qq', 'jiekuan', ['qq'], unique=False)
    op.create_table('car',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('card_struct_no', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('card_no', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('gender', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('tel', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('province', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('city', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('address', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('post_no', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('birth', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('work', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('salary', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('married', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('education_level', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('car_brand', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('car_service', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('car_config', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('color', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('engine', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_car_tel', 'car', ['tel'], unique=False)
    op.create_index('ix_car_email', 'car', ['email'], unique=False)
    op.create_table('kfc',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('card_no', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('descriot', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('ctf_tp', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('ctf_id', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('gender', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('birthday', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('address', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('zip', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('dirty', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('district1', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('district2', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('district3', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('district4', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('district5', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('district6', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('first_name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('last_name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('duty', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('mobile', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('tel', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('fax', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('nation', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('taste', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('education', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('company', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('c_tel', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('c_address', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('c_zip', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('family', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('version', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('origin_id', mysql.VARCHAR(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_kfc_tel', 'kfc', ['tel'], unique=False)
    op.create_index('ix_kfc_email', 'kfc', ['email'], unique=False)
    op.create_table('shunfeng',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('tel', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('province', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('city', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('dist', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('addr', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_shunfeng_tel', 'shunfeng', ['tel'], unique=False)
    op.create_table('qiye',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('tel', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('phone', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('company_name', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('company_address', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('province', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('company_keyword', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_qiye_tel', 'qiye', ['tel'], unique=False)
    # ### end Alembic commands ###
